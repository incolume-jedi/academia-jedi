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
    """Run it.

    Leitura de multiplos arquivos com senha.
    """
    logging.debug(filezip_sample.parts)

    for filename in ['hello.txt', 'new_hello.txt']:
        logging.debug('filename: %s', filename)
        with zipfile.ZipFile(
            filezip_sample,
            mode='r',
        ) as archive:
            for line in archive.read(filename, pwd=b'secret1').split(b'\n'):
                logging.debug('lines: %s', line)
                print(line)


if __name__ == '__main__':
    run()
