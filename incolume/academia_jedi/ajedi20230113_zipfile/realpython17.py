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
    logging.debug(directory.parts)

    with zipfile.ZipFile(directory / "sample.zip", mode="r") as archive:
        with archive.open("hello.txt", mode="r") as hello:
            for line in io.TextIOWrapper(hello, encoding="utf-8"):
                print(line.strip())


if __name__ == "__main__":
    run()
