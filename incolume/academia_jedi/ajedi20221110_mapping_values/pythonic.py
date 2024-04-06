"""Example pythonic."""
from incolume.academia_jedi.ajedi20221110_mapping_values.database import (
    get_client_list,
)

clientes = get_client_list(count=10)

if __name__ == '__main__':  # pragma: no cover
    print(clientes)  # noqa: T201
