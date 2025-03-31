"""Module."""

import logging
import zipfile

from incolume.academia_jedi.ajedi20230113_zipfile import base_dir

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)


def run():
    """Run it."""
    filenames = base_dir.rglob('*.txt')

    with zipfile.ZipFile(
        base_dir.joinpath('output_dir', 'multiple_files.zip'),
        mode='w',
    ) as archive:
        for filename in filenames:
            archive.write(filename)


if __name__ == '__main__':
    run()
