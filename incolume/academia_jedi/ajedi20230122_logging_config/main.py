import logging

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
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
