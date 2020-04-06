from __future__ import absolute_import
import logging

from django.apps import AppConfig

log = logging.getLogger(__name__)


class AlgoConfig(AppConfig):
    name = 'algo'

    def ready(self):
        from .indicies import Calculation
        try:
            if not Calculation._index.exists():
                Calculation.init()

        except Exception as e:
            log.warn(f'An error while starting algo django app: {e}')
