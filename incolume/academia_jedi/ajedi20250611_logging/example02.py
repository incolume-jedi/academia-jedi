import logging
from logging.config import fileConfig
from logging.config import dictConfig
from pathlib import Path
from icecream import ic

def load_conf_ini():
    """Example Configuration via an INI File."""
    logconf = Path(__file__).parents[3].joinpath('settings/logging_config.ini')


    fileConfig(logconf)
    logger = logging.getLogger()
    logger.info(ic(logconf))
    logger.debug('often makes a very good meal of %s', 'visiting tourists')

def load_conf_dict():
    """Example Configuration via a Dictionary.
    As of Python 2.7, you can use a dictionary with configuration details. PEP 391 contains a list of the mandatory and optional elements in the configuration dictionary.
"""
    logging_config = dict(
        version = 1,
        formatters = {
            'f': {'format':
                  '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
            },
        handlers = {
            'h': {'class': 'logging.StreamHandler',
                  'formatter': 'f',
                  'level': logging.DEBUG}
            },
        root = {
            'handlers': ['h'],
            'level': logging.DEBUG,
            },
    )

    dictConfig(logging_config)

    logger = logging.getLogger()
    logger.info(ic(logging_config))
    logger.debug('often makes a very good meal of %s', 'visiting tourists')
