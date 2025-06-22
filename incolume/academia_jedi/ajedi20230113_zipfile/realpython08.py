"""Module."""

import datetime
import zipfile

from config import settings
from incolume.academia_jedi.ajedi20230113_zipfile import filezip_sample
from pytz import timezone


def run():
    """Run it."""
    with zipfile.ZipFile(filezip_sample, mode='r') as archive:
        for info in archive.infolist():
            print(f'Filename: {info.filename}')
            timestamp = datetime.datetime(
                *info.date_time,
                tzinfo=timezone(settings.tz),
            )
            print(f'Modified: {timestamp}')
            print(f'Normal size: {info.file_size} bytes')
            print(f'Compressed size: {info.compress_size} bytes')
            print('-' * 20)


if __name__ == '__main__':
    run()
