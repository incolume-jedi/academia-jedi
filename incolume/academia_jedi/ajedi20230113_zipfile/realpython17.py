"""Module."""

import io
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
    logging.debug(filezip_sample.parts)

    with (
        zipfile.ZipFile(filezip_sample, mode='r') as archive,
        archive.open('hello.txt', mode='r') as hello,
    ):
        for line in io.TextIOWrapper(hello, encoding='utf-8'):
            print(line.strip())


if __name__ == '__main__':
    run()
