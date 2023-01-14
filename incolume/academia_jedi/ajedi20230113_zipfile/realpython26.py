import zipfile
from pathlib import Path
import datetime
import logging
import io
import tempfile

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s;%(levelname)-8s;%(name)s;"
           "%(module)s;%(funcName)s;%(message)s",
)

root = Path(__file__).parent
logging.debug(root)


def run():
    with zipfile.ZipFile(root / "sample.zip", mode="r") as archive:
        logging.debug('Readed %s', archive.filename)
        for file in archive.namelist():
            if file.endswith(".md"):
                logging.debug('Extracted "%s" into "new_output_dir/"', file)
                archive.extract(file, root / "new_output_dir/")


if __name__ == "__main__":
    run()
