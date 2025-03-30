"""Module."""

import logging
import zipfile

from incolume.academia_jedi.ajedi20230113_zipfile import filezip_sample

# ruff: noqa: T201

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)


def run():
    """Run it."""
    archive = zipfile.ZipFile(filezip_sample, mode='r')

    # Use archive in different parts of your code
    print(archive.printdir())

    # Close the archive when you're done
    archive.close()
    print(archive)


if __name__ == '__main__':
    run()
