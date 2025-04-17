"""Module."""

import zipfile
from collections.abc import Generator
from pathlib import Path

from icecream import ic
from incolume.academia_jedi.ajedi20230113_zipfile import base_dir, logger

directory = base_dir / 'output_dir'
directory.mkdir(exist_ok=True, parents=True)
logger.debug(ic('%s %s', directory, directory.exists()))

root = base_dir / 'root_dir'
root.mkdir(exist_ok=True, parents=True)
logger.debug(ic('%s %s', root, root.exists()))


def append_member(zip_file, member):
    """Append member into zipfile."""
    with zipfile.ZipFile(zip_file, mode='a') as archive:
        logger.debug('Appended %s into %s', zip_file, archive.filename)
        archive.write(member)


def get_file_from_stream(path: Path) -> Generator:
    """Simulate a stream of files."""
    yield from path.rglob('**/*.md')


def increment_zip(
    zipname: Path | str = '',
    directory: Path = directory,
) -> None:
    """Increment files into zip."""
    zipname = zipname or root / 'incremental.zip'
    zipname = Path(zipname)

    for filename in get_file_from_stream(directory):
        append_member(zipname, filename)

    with zipfile.ZipFile(zipname, mode='r') as archive:
        archive.printdir()


def run():
    """Run it."""
    increment_zip()


if __name__ == '__main__':
    run()
