from database import get_client_list
from pprint import pprint

clientes = get_client_list(count=20)

if __name__ == "__main__":  # pragma: no cover
    pprint(clientes)
