"""Example not pythonic."""

from pprint import pprint

from incolume.academia_jedi.ajedi20221110_mapping_values.database import (
    get_client_list,
)

clientes = get_client_list(count=20)

if __name__ == '__main__':  # pragma: no cover
    pprint(clientes)  # noqa: T203
