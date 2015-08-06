# In production set the environment variable like this:
#    DJANGO_SETTINGS_MODULE=tyndale.settings.production
from .base import *             # NOQA
import logging.config

# For security and performance reasons, DEBUG is turned off
DEBUG = False
TEMPLATE_DEBUG = False

# Must mention ALLOWED_HOSTS in production!
# ALLOWED_HOSTS = ["tyndale.com"]

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#
# ADMINS = (('Taehwan', 'builtbyevo@gmail.com'),)
#
# SERVER_EMAIL = 'evo@byevo.com'
#
# ALLOWED_HOSTS = ['.byevo.com',
#                  '.taedori-staging.com',
#                  'localhost']
#
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_HOST_USER = env('EMAIL_ADDRESS')
# EMAIL_HOST_PASSWORD = env('EMAIL_PASSWORD')
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True


# Cache the templates in memory for speed-up
loaders = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]

TEMPLATES[0]['OPTIONS'].update({"loaders": loaders})
TEMPLATES[0].update({"APP_DIRS": False})

# Define STATIC_ROOT for the collectstatic command

# Log everything to the logs directory at the top
LOGFILE_ROOT = join(dirname(BASE_DIR), 'logs')

# Reset logging
LOGGING_CONFIG = None
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(pathname)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'proj_log_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': join(LOGFILE_ROOT, 'project.log'),
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        }
    },
    'loggers': {
        'project': {
            'handlers': ['proj_log_file'],
            'level': 'DEBUG',
        },
    }
}

logging.config.dictConfig(LOGGING)

try:
    from .local import *
except ImportError:
    pass