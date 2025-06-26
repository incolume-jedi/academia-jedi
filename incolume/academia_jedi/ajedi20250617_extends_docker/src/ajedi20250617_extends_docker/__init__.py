"""Module for ajedi20250617-extends-docker."""
from __future__ import annotations

from icecream import ic
import os


DEBUG = os.environ.get('INCOLUME_MODE')

ic.disable()
if DEBUG:
    ic.enable()

def main() -> str:
    """Hello from ajedi20250617-extends-docker."""
    return ic('Hello from ajedi20250617-extends-docker!')


if __name__ == '__main__':
    main()
 