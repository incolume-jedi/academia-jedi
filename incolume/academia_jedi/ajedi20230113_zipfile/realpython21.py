import zipfile
from pathlib import Path
import datetime
import logging
import io

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s;%(levelname)-8s;%(name)s;"
           "%(module)s;%(funcName)s;%(message)s",
)

directory = Path(__file__).parent


def run():
    filenames = directory.rglob('*.txt')

    with zipfile.ZipFile(directory / "multiple_files.zip",
                         mode="w") as archive:
        for filename in filenames:
            archive.write(filename)


if __name__ == "__main__":
    run()
