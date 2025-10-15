"""Module."""

import contextlib
import tempfile
from pathlib import Path
from subprocess import Popen
from typing import Any

from icecream import ic

from .utils import config
from .example0 import html_text, automation1


def main() -> None:
    """Run it."""
    ic('Hello from ajedi20251013-getting-elements-in-a-table-with-playwright!')
    site = config()
    with contextlib.suppress(FileNotFoundError):
        Popen(f'python -m http.server 8000 -d {site.parent}', shell=True)
    ic(html_text)
    automation1()


if __name__ == '__main__':
    main()
