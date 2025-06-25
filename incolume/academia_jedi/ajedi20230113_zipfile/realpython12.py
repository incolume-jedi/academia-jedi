"""Module."""

import zipfile

from incolume.academia_jedi.ajedi20230113_zipfile import (
    filezip_sample_pwd,
    logger,
)


def run():
    """Run it.

    Leitura de todos os arquivos cifrados contidos no zipfile.
    """
    logger.debug(filezip_sample_pwd.parts)
    with zipfile.ZipFile(filezip_sample_pwd) as archive:
        archive.setpassword(b'secret')
        for file in archive.namelist():
            print(file)
            print('-' * 20)
            for line in archive.read(file).split(b'\n'):
                print(line)


if __name__ == '__main__':
    run()
