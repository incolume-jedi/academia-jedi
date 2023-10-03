import zipfile
from pathlib import Path
import datetime
import logging
import io


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)

directory = Path(__file__).parent


def run():
    """Extracting Member Files From Your ZIP Archives."""
    logging.debug(directory.parts)

    with zipfile.ZipFile(directory / 'sample.zip', mode='r') as archive:
        archive.extractall(directory / 'output_dir/')


if __name__ == '__main__':
    run()
