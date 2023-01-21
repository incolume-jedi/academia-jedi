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
    with zipfile.ZipFile(directory / "sample_pwd.zip") as archive:
        archive.setpassword(b"secret")
        for file in archive.namelist():
            print(file)
            print("-" * 20)
            for line in archive.read(file).split(b"\n"):
                print(line)


if __name__ == "__main__":
    run()
