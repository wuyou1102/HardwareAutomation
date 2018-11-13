# -*- encoding:UTF-8 -*-
import logging.config
import os
import sys

__LOG = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), "log", "console")
if not os.path.exists(__LOG):
    os.makedirs(__LOG)

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(__LOG, 'Debug.txt'),
            'formatter': 'verbose',
            'encoding': 'utf8',
        }
    },
    'loggers': {
        '': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
        },
    }
})
