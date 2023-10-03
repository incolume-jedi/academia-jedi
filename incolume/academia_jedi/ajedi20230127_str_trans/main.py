"""Main Module."""
import logging
from ex1 import tratativa1


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)


def run():
    """Run main module."""
    tratativa1()


if __name__ == '__main__':
    run()
