import zipfile
from pathlib import Path
import datetime

directory = Path(__file__).parent


def run():
    with zipfile.ZipFile(directory / "sample.zip", mode="r") as archive:
        for info in archive.infolist():
            print(f"Filename: {info.filename}")
            print(f"Modified: {datetime.datetime(*info.date_time)}")
            print(f"Normal size: {info.file_size} bytes")
            print(f"Compressed size: {info.compress_size} bytes")
            print("-" * 20)


if __name__ == "__main__":
    run()
