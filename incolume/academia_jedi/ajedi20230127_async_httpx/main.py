"""Main Module."""
import logging
import platform
import sys

import ex1

if sys.version_info < (3, 8):
    raise Exception(
        f'Incompatible python version. Current {platform.python_version()}.'
        f' minimal Python 3.8+'
    )

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
