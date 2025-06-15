"""Logging in an Application."""

from icecream import ic
from incolume.academia_jedi.ajedi20250611_logging.example01 import staff
from incolume.academia_jedi.ajedi20250611_logging.examples import load_conf_ini, load_conf_dict


def main() -> str:
    """Logging in an Application."""
    staff()
    load_conf_ini()
    load_conf_dict()
    return 'Hello from ajedi20250614-logging!'


if __name__ == '__main__':
    ic(main())
