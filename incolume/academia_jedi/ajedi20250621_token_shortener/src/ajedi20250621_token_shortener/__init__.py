"""Module ajedi20250621_token_shortener."""

from __future__ import annotations

import os

from icecream import ic

DEBUG = bool(os.environ.get('DEBUG_MODE'))
ic.disable()
if DEBUG:
    ic.enable()


def main() -> None:
    """Main ajedi20250621_token_shortener."""
    ic('Hello from ajedi20250621-token-shortener!')


if __name__ == '__main__':
    main()

