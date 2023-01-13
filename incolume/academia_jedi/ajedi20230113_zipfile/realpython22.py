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


if __name__ == "__main__":

    source = Path(directory/"output_dir/")

    with zipfile.ZipFile(directory/"directory.zip", mode="w") as archive:
       for file_path in source.iterdir():
           archive.write(file_path, arcname=file_path.name)


    with zipfile.ZipFile(directory/"directory.zip", mode="r") as archive:
        archive.printdir()