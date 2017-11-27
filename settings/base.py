from __future__ import unicode_literals

import os
import logging.config
from distutils.util import strtobool

ENV = os.environ.get('ENV', 'LOCAL')

DEBUG = strtobool(os.environ.get('DEBUG', 'True'))
SECRET_KEY = os.environ.get('SECRET_KEY', '84ugfvbuhjRRmefdshwjtio0234t5fwWkqa')
PROJECT_NAME = 's-alerts-notifications'

CONSOLE_LOG_LEVEL = os.environ.get('CONSOLE_LOG_LEVEL', 'INFO')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] %(name)s %(levelname)s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': CONSOLE_LOG_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
}

logging.config.dictConfig(LOGGING)

AWS_REGION = os.environ.get('AWS_REGION', 'eu-west-1')
