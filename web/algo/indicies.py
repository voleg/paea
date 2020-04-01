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


    def get_params(self):
        params = {}
        for p in self.params:
            # type p: algo.indices.Params
            key = p.name
            val = p.value
            if key:
                params.update({key: val})

        return params

    def run(self):
        return celery_app.send_task(
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

        qs = self.search.query(Q('bool', must=must_q))
        return AttrDict({
            'total': qs.count(),
            'scroll': qs.scan(),
            'search': qs,
        })
