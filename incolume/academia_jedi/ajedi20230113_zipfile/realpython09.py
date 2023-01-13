import zipfile
from pathlib import Path
import datetime


directory = Path(__file__).parent


if __name__ == "__main__":
    with zipfile.ZipFile(directory/"sample.zip", mode="r") as archive:
        for filename in archive.namelist():
            print(filename)