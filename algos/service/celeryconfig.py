import logging
import logging.config

from celery import Celery

import service.settings as settings

try:
    logging.config.dictConfig(settings.LOGGING)
    logging.info('Logging configured')
except Exception as e:
    print('Logging could not be configured: %s' % e)

app = Celery('algos')
app.config_from_object('service.settings')
