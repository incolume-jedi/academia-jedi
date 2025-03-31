"""Module."""

import logging
import zipfile
from pprint import pprint

from incolume.academia_jedi.ajedi20230113_zipfile import (
    filezip_sample,
)

# ruff:noqa:T203
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)


def run():
    """Run it."""
    files = zipfile.Path(filezip_sample)
    pprint(list(files.iterdir()))


if __name__ == '__main__':
    run()
