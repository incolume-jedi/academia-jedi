"""Logging in an Application."""

from icecream import ic
from ajedi20250611_logging.example01 import staff


def main() -> str:
    """Logging in an Application."""
    staff()

    return 'Hello from ajedi20250614-logging!'


if __name__ == '__main__':
    ic(main())
