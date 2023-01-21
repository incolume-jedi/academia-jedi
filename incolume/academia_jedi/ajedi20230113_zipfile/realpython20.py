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
    archive = zipfile.ZipFile(directory / "sample.zip", mode="r")

    # Use archive in different parts of your code
    print(archive.printdir())

    # Close the archive when you're done
    archive.close()
    print(archive)


if __name__ == "__main__":
    run()
