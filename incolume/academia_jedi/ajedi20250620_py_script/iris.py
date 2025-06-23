#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///

import urllib.request

def main() -> None:
    """Chamada script iris."""

    print("Hello from iris.py!")

    urllib.request.urlretrieve(
        "https://archive.ics.uci.edu/static/public/53/iris.zip",
        "iris.zip"
    )

    print("Downloaded iris.zip")


if __name__ == "__main__":
    main()
