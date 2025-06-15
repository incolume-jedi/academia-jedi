"""Logging in an Application."""

from icecream import ic
from incolume.academia_jedi.ajedi20250611_logging.examples import (
    load_conf_dict,
    load_conf_from_code,
    load_conf_ini,
    load_conf_file,
    staff,
    load_conf_yml,
    load_conf_yaml,
    load_conf_yaml_1,
)


def main() -> str:
    """Logging in an Application."""
    staff()
    load_conf_ini()
    load_conf_dict()
    load_conf_from_code()
    load_conf_file()
    load_conf_yml()
    load_conf_yaml()
    load_conf_yaml_1()
    return 'Hello from ajedi20250614-logging!'


if __name__ == '__main__':
    ic(main())
