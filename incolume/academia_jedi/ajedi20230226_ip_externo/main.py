"""Main Module."""

import logging

import external_ip
import tratativas

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)


def run():
    """Run main module."""
    logging.debug('starting ..')
    external_ip.run()
    tratativas.run()


if __name__ == '__main__':
    run()
