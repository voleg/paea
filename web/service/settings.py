import configparser
import os
from kombu import Exchange, Queue


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config_dev_path = os.path.join(BASE_DIR, 'deploy/settings_dev.conf')
config_prod_path = '/etc/algo_web/settings.conf'

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
    'django.contrib.staticfiles' if DEBUG else '',
    'rest_framework',
    'algos'
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

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


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

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
CELERY_TIMEZONE = 'UTC'
CELERY_RESULT_BACKEND = f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'

# CELERY STUFF
CELERY_DEFAULT_QUEUE = config_get('celery', 'CELERY_DEFAULT_QUEUE')
CELERY_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default'),
    Queue('results', Exchange('results'), routing_key='results'),
)

CELERYD_HIJACK_ROOT_LOGGER = True

CELERYD_MAX_MEMORY_PER_CHILD = 4 * 1024 * 1024  # 4GB
CELERYD_MAX_TASKS_PER_CHILD = 4

ELASTICSEARCH = {
    'HOSTS': [
        config_get('elasticsearch', 'host'),
    ]
}

