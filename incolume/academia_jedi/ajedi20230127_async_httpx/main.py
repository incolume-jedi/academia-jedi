"""Main Module."""

import logging

import ex1

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)


def run():
    """Run main module."""
    ex1.run()


if __name__ == '__main__':
    run()
