"""Module."""

import zipfile

from incolume.academia_jedi.ajedi20230113_zipfile import (
    base_dir,
    filezip_sample,
    logger,
)


def run():
    """Extracting Member Files From Your ZIP Archives."""
    logger.debug(filezip_sample.parts)

    with zipfile.ZipFile(filezip_sample, mode='r') as archive:
        archive.extractall(base_dir / 'output_dir')


if __name__ == '__main__':
    run()
