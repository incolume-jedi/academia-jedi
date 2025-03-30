"""Module."""

import logging
import zipfile

from icecream import ic
from incolume.academia_jedi.ajedi20230113_zipfile import base_dir

ic()

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)


directory = base_dir / 'output_dir'
directory.mkdir(exist_ok=True, parents=True)
logging.debug(ic('%s %s', directory, directory.exists()))

root = base_dir / 'root_dir'
root.mkdir(exist_ok=True, parents=True)
logging.debug(ic('%s %s', root, root.exists()))


def run():
    """Descompactar o sample.zip em /tmp/root_dir."""
    with zipfile.ZipFile(root / 'directory_tree.zip', mode='w') as archive:
        for file_path in directory.rglob('*'):
            archive.write(file_path, arcname=file_path.relative_to(directory))

    with zipfile.ZipFile(root / 'directory_tree.zip', mode='r') as archive:
        archive.printdir()


if __name__ == '__main__':
    run()
