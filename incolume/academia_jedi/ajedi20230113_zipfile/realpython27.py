"""Module."""

import logging
import zipfile
from pathlib import Path

from incolume.academia_jedi.ajedi20230113_zipfile import (
    filezip_sample,
)

# ruff: noqa: T201

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)

root = Path(__file__).parent
logging.debug(root)


def run():
    """Run it."""
    logging.debug('Creted object zipfile to handler')
    hello_txt = zipfile.Path(filezip_sample, 'hello.txt')
    print(
        hello_txt,
        hello_txt.name,
        hello_txt.is_file(),
        hello_txt.exists(),
        hello_txt.read_text(),
        sep='\n',
    )


if __name__ == '__main__':
    run()
