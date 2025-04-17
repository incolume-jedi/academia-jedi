"""Module."""

import zipfile
from pathlib import Path

from incolume.academia_jedi.ajedi20230113_zipfile import base_dir

hello = Path(base_dir, 'hello.txt')
hello.write_text('hello again.')


def tratativa(filename: Path, filenamezip: Path) -> Path:
    """Estudos sobre zipfile."""
    with zipfile.ZipFile(filenamezip, mode='w') as archive:
        archive.write(filename)
    return filenamezip


def run():
    """Run it."""
    tratativa(hello, 'missing/hello.zip')


if __name__ == '__main__':
    run()
