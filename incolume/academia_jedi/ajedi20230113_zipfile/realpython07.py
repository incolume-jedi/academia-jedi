"""Module."""

import zipfile
from pathlib import Path

from incolume.academia_jedi.ajedi20230113_zipfile import base_dir

# ruff: noqa: T201

hello = Path(base_dir, 'hello.txt')
hello.write_text(__file__)
hello.with_stem('new_hello').write_text('hello again.')


def run():
    """Run it."""
    with zipfile.ZipFile(hello.parent / 'hello.zip', mode='r') as archive:
        print(archive.infolist())
        print(archive.namelist())
        print(hello.parent)

        info = archive.getinfo(Path(*hello.parts[1:]).as_posix())
    print(
        f'{info.file_size=}\n{info.compress_size=}\n{info.filename=}\n{info.date_time=}\n',
    )


if __name__ == '__main__':
    run()
