import zipfile
from pathlib import Path
import datetime
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s;%(levelname)-8s;%(name)s;"
           "%(module)s;%(funcName)s;%(message)s",
)

directory = Path(__file__).parent


def run():
    logging.debug(directory.parts)

    with zipfile.ZipFile(directory / "sample.zip", mode="r") as archive:
        logging.debug(archive.filename)
        text = archive.read("hello.txt").decode(encoding="utf-8")

    print(text)


if __name__ == "__main__":
    run()
