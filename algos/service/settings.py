import configparser
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config_dev_path = os.path.join(BASE_DIR, 'deploy/settings_dev.conf')
config_prod_path = '/code/deploy/settings.conf'

config = configparser.RawConfigParser()
config.read((config_dev_path, config_prod_path))

_config_check = lambda x, y: config.has_section(x) and config.has_option(x, y)
config_get = lambda x, y, z=None, method=config.get: _config_check(x, y) and method(x, y) or z

DEBUG = config_get('app', 'DEBUG', False, method=config.getboolean)

# Celery config
worker_hijack_root_logger=False
broker_url = config_get('celery', 'BROKER')
result_backend = config_get('celery', 'RESULT_BACKEND')
accept_content = ['json']
task_default_queue='algos'
imports = ('service.tasks',)
task_ignore_result=True
worker_prefetch_multiplier=10
worker_max_tasks_per_child=100
task_store_errors_even_if_ignored=True
task_acks_late=True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s %(pathname)s:%(lineno)d] %(levelname)s: %(message)s'
        },
        'simple': {
            'format': '[%(asctime)s %(name)s %(module)s] %(levelname)s: %(message)s'
        },
        'msg': {
            'format': '%(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'INFO',
        },
        'celery': {
            'handlers': ['console'],
            'propagate': False
        },
        'celery.task': {
            'handlers': ['console'],
        },
    },
}
