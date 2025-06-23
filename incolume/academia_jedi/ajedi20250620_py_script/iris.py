#!/usr/bin/env python3
"""Script iris."""
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///

import urllib.request


def main() -> None:
    """Chamada script iris."""
    print('Hello from script iris.py!')

    IRIS_DATA_URL = 'https://archive.ics.uci.edu/static/public/53/iris.zip'
    LOCAL_ZIP_FILENAME = 'iris.zip'

    urllib.request.urlretrieve(IRIS_DATA_URL, LOCAL_ZIP_FILENAME)

    print(f'Downloaded {LOCAL_ZIP_FILENAME}')


if __name__ == '__main__':
    main()
