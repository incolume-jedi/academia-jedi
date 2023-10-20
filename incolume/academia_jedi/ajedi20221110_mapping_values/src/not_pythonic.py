from pprint import pprint

from database import get_client_list

clientes = get_client_list(count=20)

if __name__ == '__main__':  # pragma: no cover
    pprint(clientes)
