"""Module."""

import logging
import zipfile

from incolume.academia_jedi.ajedi20230113_zipfile import base_dir

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)

source = base_dir / 'output_dir'
fout = base_dir / 'directory.zip'


def run():
    """Run it."""
    with zipfile.ZipFile(fout, mode='w') as archive:
        logging.debug('Create %s', archive.filename)
        for file_path in source.iterdir():
            archive.write(file_path, arcname=file_path.name)

    with zipfile.ZipFile(fout, mode='r') as archive:
        logging.debug('Read %s', archive.filename)
        archive.printdir()


if __name__ == '__main__':
    run()
