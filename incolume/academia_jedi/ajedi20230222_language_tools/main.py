"""Main Module."""
import logging

from tratativa1 import run as run1

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)


def run():
    """Run main module."""
    logging.debug('starting ..')
    run1()


if __name__ == '__main__':
    run()
