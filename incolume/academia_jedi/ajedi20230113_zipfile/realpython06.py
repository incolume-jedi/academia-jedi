"""Module."""

import zipfile
from pathlib import Path

from incolume.academia_jedi.ajedi20230113_zipfile import base_dir, outputdir

hello = Path(base_dir, 'hello.txt')
hello.write_text('hello')
hello.with_stem('new_hello').write_text('hello again.')


def run():
    """Run it."""
    fout: Path = outputdir / hello.with_suffix('.zip').name
    with zipfile.ZipFile(fout, mode='a') as archive:
        archive.write(hello.parent / 'new_hello.txt')

    with zipfile.ZipFile(fout) as archive:
        archive.printdir()


if __name__ == '__main__':
    run()
