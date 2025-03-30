"""Module."""

import logging
import zipfile
from pathlib import Path

from incolume.academia_jedi.ajedi20230113_zipfile import (
    base_dir,
    filezip_sample,
)

# ruff: noqa: T201

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)


def run():
    """Extracting Member Files From Your ZIP Archives."""
    logging.debug(filezip_sample.parts)

    with zipfile.ZipFile(filezip_sample, mode='r') as archive:
        archive.extract(
            'wzxnlQNFSlVoPJe.md',
            path=Path(base_dir, 'output_dir'),
        )


if __name__ == '__main__':
    run()
