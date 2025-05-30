"""Main Module."""

import logging

from incolume.academia_jedi.ajedi20230226_operador_morsa import (
    exemplo1,
    exemplo2,
)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)


def run():
    """Run main module."""
    logging.debug('starting ..')
    exemplo1.run()
    exemplo2.run()


if __name__ == '__main__':
    run()
