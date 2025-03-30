"""Module."""

import zipfile
from pathlib import Path
from tempfile import gettempdir

directory = Path(__file__).parent

hello = Path(gettempdir(), 'hello.txt')
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
