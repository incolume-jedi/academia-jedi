"""Module."""

import zipfile

from icecream import ic
from incolume.academia_jedi.ajedi20230113_zipfile import base_dir, logger

directory = base_dir / 'output_dir'
directory.mkdir(exist_ok=True, parents=True)
logger.debug(ic('%s %s', directory, directory.exists()))

root = base_dir / 'root_dir'
root.mkdir(exist_ok=True, parents=True)
logger.debug(ic('%s %s', root, root.exists()))


def run():
    """Run it.

    Nível de compressão do arquivo zip.
    """
    with zipfile.ZipFile(
        root / 'comp_dir.zip',
        'w',
        zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as archive:
        logger.debug('Created %s', archive.filename)
        for file_path in directory.rglob('*'):
            logger.debug('Added %s', file_path)
            archive.write(file_path, arcname=file_path.relative_to(directory))


if __name__ == '__main__':
    run()
