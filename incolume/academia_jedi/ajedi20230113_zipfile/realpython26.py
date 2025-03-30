"""Module."""

import logging
import zipfile

from incolume.academia_jedi.ajedi20230113_zipfile import (
    base_dir,
    filezip_sample,
)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)


def run():
    """Run it."""
    with zipfile.ZipFile(filezip_sample, mode='r') as archive:
        logging.debug('Readed %s', archive.filename)
        for file in archive.namelist():
            if file.endswith('.md'):
                logging.debug('Extracted "%s" into "new_output_dir/"', file)
                archive.extract(file, base_dir / 'new_output_dir/')


if __name__ == '__main__':
    run()
