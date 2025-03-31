"""Module."""

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
    """Run it.

    Leitura de todos os arquivos cifrados contidos no zipfile.
    """
    logging.debug(filezip_sample_pwd.parts)
    with zipfile.ZipFile(filezip_sample_pwd) as archive:
        archive.setpassword(b'secret')
        for file in archive.namelist():
            print(file)
            print('-' * 20)
            for line in archive.read(file).split(b'\n'):
                print(line)


if __name__ == '__main__':
    run()
