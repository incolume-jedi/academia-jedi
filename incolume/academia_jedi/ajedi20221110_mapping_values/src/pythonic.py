from database import get_client_list

clientes = get_client_list(count=2)

if __name__ == "__main__":  # pragma: no cover
    print(clientes)
