import logging
from datetime import datetime
from django.conf import settings
from elasticsearch_dsl import (
    Date,
    Document,
    Integer,
    Text,
    InnerDoc,
    connections,
    Q,
    AttrDict
)

log = logging.getLogger(__name__)

connections.create_connection(hosts=settings.ELASTICSEARCH['HOSTS'], timeout=20)


class Status:
    accepted = 'accepted'
    complete = 'complete'
    error = 'error'


class Calculation(Document):
    # _id = Integer()
    func_name = Text()
    params = InnerDoc(enabled=False)   # just store it w/o indexing
    created_at = Date()
    results = InnerDoc()

    class Index:
        name = 'calculations'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    def run(self):
        # TODO: add here calculation task execution celery.send_task
        return

    def save(self, **kwargs):
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
