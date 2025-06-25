"""Module."""

import datetime as dt
import re
import zipfile
from pathlib import Path

from config import settings
from icecream import ic
from incolume.academia_jedi.ajedi20230113_zipfile import (
    base_dir,
    filezip_sample,
    logger,
)
from pytz import timezone

file_test: Path = Path(base_dir, Path(__file__).stem).with_suffix('.zip')
file_test.write_bytes(filezip_sample.read_bytes())
ic(file_test)

timestamp: dt.datetime = dt.datetime.now(tz=timezone(settings.tz))

filename = 'new_hello_{}.txt'.format(
    re.sub(r'[:\.]', '-', timestamp.isoformat()),
)
ic(filename)


def run():
    """Run it.

    Acrescenado  arquivos os container zip.
    """
    logger.debug(file_test.parts)

    with (
        zipfile.ZipFile(file_test, mode='a') as archive,
        archive.open(filename, 'w') as new_hello,
    ):
        new_hello.write(
            bytes(
                f'Hello, World! (in {timestamp})',
                encoding='utf-8',
            ),
        )

    with zipfile.ZipFile(file_test, mode='r') as archive:
        archive.printdir()
        print('------')
        print(archive.read(filename))


if __name__ == '__main__':
    run()
