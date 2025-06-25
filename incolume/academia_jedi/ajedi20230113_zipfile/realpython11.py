"""Module.

Estudo de arquivos zipados com senha.
"""

import zipfile

from incolume.academia_jedi.ajedi20230113_zipfile import (
    filezip_sample_pwd,
    logger,
)


def run():
    """Run it."""
    logger.debug(filezip_sample_pwd.parts)

    try:
        with zipfile.ZipFile(
            filezip_sample_pwd,
            mode='r',
        ) as archive:
            logger.debug(archive.namelist())
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
        logger.exception(e.__cause__)


if __name__ == '__main__':
    run()
