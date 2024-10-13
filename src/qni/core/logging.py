import logging
import logging.config

logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'level': 'DEBUG'
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'qni_core.log',
            'formatter': 'default',
            'level': 'INFO'
        }
    },
    'loggers': {
        'qni_core': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG'
        }
    }
})

logger = logging.getLogger('qni_core')

def log_debug(message):
    logger.debug(message)

def log_info(message):
    logger.info(message)

def log_warning(message):
    logger.warning(message)

def log_error(message):
    logger.error(message)

def log_critical(message):
    logger.critical(message)
