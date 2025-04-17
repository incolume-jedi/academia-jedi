"""Main Module."""

import logging

from incolume.academia_jedi.ajedi20230216_python_match import (
    exemplo1,
    exemplo2,
    exemplo3,
    exemplo4,
    exemplo5,
    exemplo6,
    exemplo7,
    exemplo8,
    exemplo9,
    exemplo10,
    exemplo11,
    exemplo12,
    exemplo13,
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
    exemplo3.run()
    exemplo4.run()
    exemplo5.run()
    exemplo6.run()
    exemplo7.run()
    exemplo8.run()
    exemplo9.run()
    exemplo10.run()
    exemplo11.run()
    exemplo12.run()
    exemplo13.run()


if __name__ == '__main__':
    run()
