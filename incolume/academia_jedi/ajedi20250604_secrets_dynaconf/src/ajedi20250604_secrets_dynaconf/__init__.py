"""Secrets management for ajedi20250604 using Dynaconf."""

from __future__ import annotations

import json

import toml
import yaml
from icecream import ic

content: str = """
default:
  password: 123@pwd

development:

production:
  password: sek@987342$

testing:
  password: 777777a

"""


def load_yaml_from_str(content: str) -> dict:
    """Load a YAML configuration file."""
    return yaml.safe_load(content)


def dumps_yaml(data: dict) -> str:
    """Dump a dictionary to a YAML string."""
    return yaml.dump(data, default_flow_style=False, sort_keys=False)


def dumps_json(data: dict) -> str:
    """Dump a dictionary to a JSON string."""
    return json.dumps(data, indent=2, ensure_ascii=False)


def dumps_toml(data: dict) -> str:
    """Dump a dictionary to a TOML string."""
    return toml.dumps(data, encoder=toml.TomlNumpyEncoder())


def main() -> None:
    """Main function to run the secrets management."""
    print('Hello from ajedi20250604-secrets-dynaconf!')  # noqa: T201
    data = load_yaml_from_str(content=content)
    ic(dumps_json(data))
    ic(dumps_yaml(data))
    ic(dumps_toml(data))


if __name__ == '__main__':
    main()
