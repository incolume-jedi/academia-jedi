"""Module."""

import zipfile
from pathlib import Path

from incolume.academia_jedi.ajedi20230113_zipfile import (
    base_dir,
    filezip_sample,
    logger,
)

# ruff: noqa: T201

hello = Path(base_dir, 'hello.txt')
hello.write_text('hello')
logger.info('created: %s', hello)

hello.with_stem('new_hello').write_text(f'{hello.read_text} hello again.')
logger.info('created: %s', hello.with_stem('new_hello'))


def run():
    """Run it.

    Conteúdo do arquivo new_hello.txt dentro do zipfile.
    """
    logger.debug(filezip_sample.parts)

    with zipfile.ZipFile(filezip_sample, mode='r') as archive:
        logger.debug(archive.namelist())
        for line in archive.read(
            hello.with_stem('new_hello').name,
        ).split(b'\n'):
            print(line)


if __name__ == '__main__':
    run()
