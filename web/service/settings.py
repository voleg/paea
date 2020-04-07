import configparser
import os
from kombu import Exchange, Queue


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config_dev_path = os.path.join(BASE_DIR, 'deploy/settings_dev.conf')
config_prod_path = '/code/deploy/settings.conf'

config = configparser.RawConfigParser()
config.read((config_dev_path, config_prod_path))

def _config_check(x, y):
    return config.has_section(x) and config.has_option(x, y)

def config_get(x, y, z=None, method=config.get):
    return _config_check(x, y) and method(x, y) or z


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config_get('main', 'SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config_get('main', 'DEBUG', False, method=config.getboolean)

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
   # 'django.contrib.admin',
   # 'django.contrib.auth',
   # 'django.contrib.contenttypes',
   # 'django.contrib.sessions',
   # 'django.contrib.messages',
    'rest_framework',
    'algo',
]

if DEBUG:
    INSTALLED_APPS += [
        'corsheaders',
        'django.contrib.staticfiles'
    ]
    CORS_ORIGIN_ALLOW_ALL = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DEBUG:
    MIDDLEWARE.insert(1, 'corsheaders.middleware.CorsMiddleware')

ROOT_URLCONF = 'service.urls'


if DEBUG:
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                ],
            },
        },
    ]

WSGI_APPLICATION = 'service.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
    'UNAUTHENTICATED_USER': None,
}

if DEBUG:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    )
else:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
        'rest_framework.renderers.JSONRenderer',
    )


# REDIS STUFF
REDIS_PORT = config_get('redis', 'REDIS_PORT')
REDIS_DB = config_get('redis', 'REDIS_DB')
REDIS_HOST = config_get('redis', 'REDIS_HOST')

# BROKER
BROKER_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'
# CELERY STUFF
CELERY_TIMEZONE = 'UTC'
CELERY_RESULT_BACKEND = f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'
CELERY_TASK_ACKS_LATE=True
CELERY_DEFAULT_QUEUE = 'default'
CELERY_IMPORTS = ('algo.tasks',)
CELERY_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default'),
    Queue('results', Exchange('results'), routing_key='results'),
)

CELERYD_HIJACK_ROOT_LOGGER = False
# CELERYD_MAX_MEMORY_PER_CHILD = 1 * 1024 * 1024
CELERYD_MAX_TASKS_PER_CHILD = 16

ELASTICSEARCH = {
    'HOSTS': [
        config_get('elasticsearch', 'host'),
    ]
}

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
            'level': 'DEBUG' if DEBUG else 'ERROR',
        },
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'ERROR',
        },
        'django.utils.autoreload': {
            # Get rid of noisy debug messages
            'handlers': ['console'],
            'level': os.environ.get('LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
        'django.template': {
            # Get rid of noisy debug messages
            'handlers': ['console'],
            'level': os.environ.get('LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
        'django.server': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'INFO'
        },
        # 'django.db.backends': {
        #    'handlers': ['console', 'sentry'],
        #    'level': 'DEBUG' if DEBUG else 'ERROR'
        # },
        'celery': {
            # 'level': 'DEBUG' if DEBUG else 'WARNING',
            'handlers': ['console'],
            'propagate': True,
        },
        'celery.task': {
            'handlers': ['console'],
            # 'level': 'DEBUG' if DEBUG else 'WARNING',
            'propagate': True,
        },
        'django.db': {
            'handlers': ['console'],
            'level': 'INFO' if DEBUG else 'WARNING',
            'propagate': False,
        },
    },
}
