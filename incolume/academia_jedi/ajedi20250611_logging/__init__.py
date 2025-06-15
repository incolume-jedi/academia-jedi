"""Logging in an Application."""

from icecream import ic
from incolume.academia_jedi.ajedi20250611_logging.example01 import staff
from incolume.academia_jedi.ajedi20250611_logging.example02 import load_conf_ini


def main() -> str:
    """Logging in an Application."""
    staff()
    load_conf_ini()
    return 'Hello from ajedi20250614-logging!'


if __name__ == '__main__':
    ic(main())
