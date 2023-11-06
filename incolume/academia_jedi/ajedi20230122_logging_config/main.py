import logging
import sys
from pathlib import Path

__author__ = '@britodfbr'  # pragma: no cover

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)


def get_logger(**kwargs):
    """:param kwargs:
    :return:
    """
    # Create a custom logger
    logger = logging.getLogger(__name__)

    # Create handlers
    c_handler = logging.StreamHandler(sys.stdout)
    c_handler.setLevel(kwargs.get('loglevelstream', logging.NOTSET))

    logfile = Path(__file__).parents[4].joinpath('logs', 'file.log')
    logfile.parent.mkdir(parents=True, exist_ok=True)
    f_handler = logging.FileHandler(kwargs.get('logfile', logfile.as_posix()))
    f_handler.setLevel(kwargs.get('loglevelfile', logging.NOTSET))

    # Create formatters and add it to handlers
    c_format = logging.Formatter(
        kwargs.get(
            'logformatstream',
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        ),
    )
    f_format = logging.Formatter(
        kwargs.get(
            'logformatfile',
            '%(asctime)s; %(levelname)-8s; %(name)s; %(module)s; '
            '%(funcName)s; %(threadName)s; %(thread)d; %(message)s',
        ),
    )
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger


def setup_applevel_logger(**kwargs):
    logger = logging.getLogger(kwargs.get('logname', __name__))
    logger.setLevel(kwargs.get('loglevel', logging.DEBUG))
    formatter = logging.Formatter(
        kwargs.get(
            'logformat',
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        ),
    )
    sh = logging.StreamHandler(sys.stdout)
    sh.setFormatter(formatter)
    logger.handlers.clear()
    logger.addHandler(sh)

    file_name = Path(kwargs.get('logfile', 'logs/file.log'))
    file_name.parent.mkdir(parents=True, exist_ok=True)
    if file_name:
        fh = logging.FileHandler(file_name.as_posix())
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    return logger


if __name__ == '__main__':  # pragma: no cover
    logger = get_logger(
        loglevelstream=logging.DEBUG,
        loglevelfile=logging.DEBUG,
    )
    logger.debug('This is a debug')
    logger.info('This is a info')
    logger.warning('This is a warning')
    logger.error('This is an error')
    logger.critical('This is a critical')

    logger1 = setup_applevel_logger(logfile='file.log', loglevel=logging.DEBUG)
    logger1.debug('This is a debug')
    logger1.info('This is a info')
    logger1.warning('This is a warning')
    logger1.error('This is an error')
    logger1.critical('This is a critical')
