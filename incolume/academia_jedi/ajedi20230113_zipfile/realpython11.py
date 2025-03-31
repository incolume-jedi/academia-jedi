"""Module.

Estudo de arquivos zipados com senha.
"""

import logging
import zipfile

from incolume.academia_jedi.ajedi20230113_zipfile import filezip_sample_pwd

# ruff: noqa: T201

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)


def run():
    """Run it."""
    logging.debug(filezip_sample_pwd.parts)

    try:
        with zipfile.ZipFile(
            filezip_sample_pwd,
            mode='r',
        ) as archive:
            logging.debug(archive.namelist())
            for line in archive.read(
                'sample/wzxnlQNFSlVoPJe.md',
                pwd=b'secret',
            ).split(b'\n'):
                print(line)

        with zipfile.ZipFile(
            filezip_sample_pwd,
            mode='r',
        ) as archive:
            for line in archive.read('sample/wzxnlQNFSlVoPJe.md').split(b'\n'):
                print(line)
    except RuntimeError as e:
        logging.exception(e.__cause__)


if __name__ == '__main__':
    run()
