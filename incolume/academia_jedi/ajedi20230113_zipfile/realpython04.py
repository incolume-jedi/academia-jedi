"""Module."""

import zipfile
from pathlib import Path
from tempfile import gettempdir

hello = Path(gettempdir(), 'hello.txt')
hello.write_text('hello')


def tratativa(filename: Path) -> Path:
    """Estudo com zipfile."""
    fout: Path = filename.with_suffix('.zip')
    with zipfile.ZipFile(fout, mode='w') as archive:
        archive.write(filename)
    return fout


def run():
    """Run it."""
    tratativa(hello)


if __name__ == '__main__':  # pragma: no cover
    run()
