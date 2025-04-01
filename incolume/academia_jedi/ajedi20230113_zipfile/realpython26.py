"""Module."""

import zipfile

from incolume.academia_jedi.ajedi20230113_zipfile import (
    base_dir,
    filezip_sample,
    logger,
)


def run():
    """Run it."""
    with zipfile.ZipFile(filezip_sample, mode='r') as archive:
        logger.debug('Readed %s', archive.filename)
        for file in archive.namelist():
            if file.endswith('.md'):
                logger.debug('Extracted "%s" into "new_output_dir/"', file)
                archive.extract(file, base_dir / 'new_output_dir/')


if __name__ == '__main__':
    run()
