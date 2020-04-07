import logging
from datetime import datetime

from django.conf import settings
from elasticsearch_dsl import (
    Date,
    Document,
    Integer,
    Text,
    InnerDoc,
    Object,
    Keyword,
    connections,
    Q,
    AttrDict
)
from celery.result import AsyncResult

from service.celeryconfig import app as celery_app


log = logging.getLogger(__name__)

connections.create_connection(hosts=settings.ELASTICSEARCH['HOSTS'], timeout=20)


class Status:
    new = 'new'
    accepted = 'accepted'
    complete = 'complete'
    error = 'error'


class Params(InnerDoc):
    name=Text()
    value=Integer()


class Calculation(Document):
    # _id = Integer()
    func_name = Text(fields={'raw': Keyword()})
    status = Text(fields={'raw': Keyword()})
    params = Object(Params)
    created_at = Date()
    results = Object()

    class Index:
        name = 'calculations'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    def get_calc_exec_time(self):
        """ extracts `execution time` of function """
        if 'result' in self and 'execution_time' in self.result:
            return self.result.execution_time

    def get_result(self, default=None):
        try:
            if self.status == Status.complete:
                return self.result.result

            if self.status == Status.error:
                return self.result.error

            # This will execute only if no other statuses recieved the valid way
            return self._process_async_failure()

        except Exception as e:
            return default

    def _process_async_failure(self):
        res = self._async_result
        if res and res.status == 'FAILURE':
            err_msg = str(self._async_result.result)
            self.update(
                status=Status.error,
                result = {'error': err_msg}
            )
            return err_msg

    def get_params(self):
        """
        transforms params suitable for execution
        for ex.: from { name: n, value: 5 } -> {n: 5}
        """
        params = {}
        for p in self.params:
            # type p: algo.indices.Params
            key = p.name
            val = p.value
            if key:
                params.update({key: val})

        return params

    def get_params_string(self, default='') -> str:
        """ creates a string representation of params """
        try:
            return (', '.join([f"{p['name']}={p['value']}" for p in self.params]))
        except Exception as e:
            return default


    def run(self) -> 'celery.result.AsyncResult':
        """
        set an execution task
        """
        task = celery_app.send_task(
            'calculate_function',
            queue='algos',
            kwargs={
                'on_result': {
                    'queue': 'results',
                    'task': 'store_calculation_result',
                },
                'options': {
                    'id': self.meta.id,
                    'func_name': self.func_name,
                    'params': self.get_params()
                },
            }
        )
        self.task_id = task.id
        self.save()
        return

    @property
    def _async_result(self):
        return AsyncResult(self.task_id)

    def get_task_status(self):
        # TODO: cache this
        if self.task_id: 
            return self._async_result.status

    def get_task_result(self):
        # TODO: cache this
        if self.task_id:
            return self._async_result.result

    def to_display(self):
        doc = self.to_dict()
        doc['id'] = self.meta.id
        doc['params_display'] = self.get_params_string()
        doc['exec_time'] = self.get_calc_exec_time()
        doc['result'] = self.get_result()
        return doc

    def save(self, **kwargs):
        self.status = Status.new
        self.created_at = datetime.now()
        return super().save(**kwargs)


class CalculationSearch(object):

    def __init__(self, limit=None):
        self.search = Calculation.search()
        self.limit = limit

    def query(self, func_name=None, created_at=None):
        must_q = []
        if func_name:
            must_q.append(Q('match', tissue={'query': func_name, 'operator': 'and'}))

        if len(must_q):
            q = Q('bool', must=must_q)
        else:
            q = Q('match_all')

        qs = self.search.sort("-created_at").query(q)

        return AttrDict({
            'total': qs.count(),
            'scroll': qs.scan(), # FIXME: does not respects sorting ...
            'search': qs,
        })
