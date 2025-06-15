"""Examples logging."""

import logging
from inspect import stack
from logging.config import dictConfig, fileConfig
from pathlib import Path
import yaml
from icecream import ic

logging.getLogger(__name__).addHandler(logging.NullHandler())


def staff():
    """Staff function."""
    logging.info('Ran %s', stack()[0][3])


def load_conf_ini():
    """Example Configuration via an INI File."""
    logconf = Path(__file__).parents[3].joinpath('settings/logging_config.ini')

    fileConfig(logconf)
    logger = logging.getLogger()
    logger.info(ic(logconf))
    logger.debug('often makes a very good meal of %s', 'visiting tourists')


def load_conf_dict():
    """Example Configuration via a Dictionary.

    As of Python 2.7, you can use a dictionary with configuration details.
    PEP 391 contains a list of the mandatory and optional elements
    in the configuration dictionary.
    """
    logging_config = dict(
        version=1,
        formatters={
            'f': {
                'format': '%(asctime)s %(name)-12s'
                ' %(levelname)-8s %(message)s',
            },
        },
        handlers={
            'h': {
                'class': 'logging.StreamHandler',
                'formatter': 'f',
                'level': logging.DEBUG,
            },
        },
        root={
            'handlers': ['h'],
            'level': logging.DEBUG,
        },
    )

    dictConfig(logging_config)

    logger = logging.getLogger()
    logger.info(ic(logging_config))
    logger.debug('often makes a very good meal of %s', 'visiting tourists')


def load_conf_from_code():
    """Example Configuration Directly in Code"""
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s;%(levelname)-8s;%(name)s;%(module)s;%(funcName)s;%(message)s',
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    logger.debug('often makes a very good meal of %s', 'visiting tourists')

def load_conf_file():
    """Configuração via conf."""
    logconf = Path(__file__).parents[3].joinpath('settings/logging.conf')

    fileConfig(ic(logconf))
    logger = logging.getLogger()
    logger.info('Tudo é difícil .%s', '. até fácil se tornar.')

def load_conf_yml():
    """Configuração via YAML."""
    with Path(__file__).parents[3].joinpath('settings/logging.yml').open('rt') as file:
        logconf = yaml.safe_load(file.read())

    dictConfig(ic(logconf))
    logger = logging.getLogger()
    logger.info('Tudo é difícil .%s', '. até fácil se tornar.')


def load_conf_yaml():
    """Configuração via YAML."""
    # Load the config file
    file = Path(__file__).parents[3].joinpath('settings/logging_conf.yml')

    with file.open('rt') as f:
        config = yaml.safe_load(f.read())

    # Configure the logging module with the config file
    dictConfig(config)

    # Get a logger object
    logger = logging.getLogger('development')

    # Log some messages
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')

def load_conf_yaml_1():
    """Configuração via YAML."""
    # Load the config file
    file = Path(__file__).parents[3].joinpath('settings/logging_conf.yml')

    with file.open('rt') as f:
        config = yaml.safe_load(f.read())

    # Configure the logging module with the config file
    dictConfig(config)

    for logger_name in ['development', 'staging', 'production']:
        # Get a logger object
        logger = logging.getLogger(logger_name)

        # Log some messages
        logger.debug('This is a debug message')
        logger.info('This is an info message')
        logger.warning('This is a warning message')
        logger.error('This is an error message')
        logger.critical('This is a critical message')

def logging_config_load(file_or_dict: dict|Path):
    """Load configuration for logging."""

