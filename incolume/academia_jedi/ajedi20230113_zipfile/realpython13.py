"""Module."""

import zipfile

from incolume.academia_jedi.ajedi20230113_zipfile import filezip_sample, logger

# ruff: noqa: T201


def run():
    """Run it.

    Leitura de multiplos arquivos com senha.
    """
    logger.debug(filezip_sample.parts)

    for filename in ['hello.txt', 'new_hello.txt']:
        logger.debug('filename: %s', filename)
        with zipfile.ZipFile(
            filezip_sample,
            mode='r',
        ) as archive:
            for line in archive.read(filename, pwd=b'secret1').split(b'\n'):
                logger.debug('lines: %s', line)
                print(line)


if __name__ == '__main__':
    run()
