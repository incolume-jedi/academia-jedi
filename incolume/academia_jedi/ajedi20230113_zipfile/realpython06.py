"""Module."""

import zipfile
from pathlib import Path

from incolume.academia_jedi.ajedi20230113_zipfile import base_dir

hello = Path(base_dir, 'hello.txt')
hello.write_text('hello')
hello.with_stem('new_hello').write_text('hello again.')


def run():
    """Run it."""
    with zipfile.ZipFile(hello.parent / 'hello.zip', mode='a') as archive:
        archive.write(hello.parent / 'new_hello.txt')

    with zipfile.ZipFile(hello.parent / 'hello.zip') as archive:
        archive.printdir()


if __name__ == '__main__':
    run()
