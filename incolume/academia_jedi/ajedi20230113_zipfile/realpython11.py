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


if __name__ == "__main__":
    logging.debug(directory.parts)

    with zipfile.ZipFile(directory/"sample_pwd.zip", mode="r") as archive:
        logging.debug(archive.namelist())
        for line in archive.read("sample/wzxnlQNFSlVoPJe.md", pwd=b"secret").split(b"\n"):
            print(line)


    with zipfile.ZipFile(directory/"sample_pwd.zip", mode="r") as archive:
        for line in archive.read("sample/wzxnlQNFSlVoPJe.md").split(b"\n"):
            print(line)
        