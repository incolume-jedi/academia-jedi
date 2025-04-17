"""Module."""

import zipfile
from pprint import pprint

from incolume.academia_jedi.ajedi20230113_zipfile import filezip_sample, logger

# ruff:noqa:T203


def run():
    """Run it."""
    files = zipfile.Path(filezip_sample)
    result = list(files.iterdir())
    logger.info(result)
    pprint(result)


if __name__ == '__main__':
    run()
