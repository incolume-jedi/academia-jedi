import zipfile
from pathlib import Path
import datetime
import logging
import io
import tempfile
from pprint import pprint


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)

root = Path(__file__).parent
logging.debug(root)


def run():
    files = zipfile.Path(root / 'sample.zip')
    pprint(list(files.iterdir()))


if __name__ == '__main__':
    run()
