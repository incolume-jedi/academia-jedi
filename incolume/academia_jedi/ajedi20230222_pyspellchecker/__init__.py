"""Main Module."""

import logging

from incolume.academia_jedi.ajedi20230222_pyspellchecker import tratativa1

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)


def run():
    """Run main module."""
    logging.debug('starting ..')
    tratativa1.ex0()
    tratativa1.ex1()


if __name__ == '__main__':
    run()
