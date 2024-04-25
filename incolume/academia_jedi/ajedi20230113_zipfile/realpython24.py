import logging
import zipfile
from pathlib import Path

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)

root = Path(__file__).parent
logging.debug(root)


def run():
    directory = Path(root / 'output_dir/')

    with zipfile.ZipFile(
        root / 'comp_dir.zip',
        'w',
        zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as archive:
        logging.debug('Created %s', archive.filename)
        for file_path in directory.rglob('*'):
            logging.debug('Added %s' % file_path)
            archive.write(file_path, arcname=file_path.relative_to(directory))


if __name__ == '__main__':
    run()
