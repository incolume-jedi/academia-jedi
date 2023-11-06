import datetime as dt
from dataclasses import dataclass
from sys import getsizeof

from faker import Faker


@dataclass
class Cliente:
    nome: str
    size_at: dt.datetime


def get_client_list(**kwargs) -> list[Cliente, ...]:
    """Return a client fake list."""
    fake = Faker(kwargs.get('lang', 'pt_Br'))
    fake.seed_instance(kwargs.get('seed', 31))

    return [
        Cliente(
            **{
                'nome': f'{fake.first_name()} {fake.last_name()} {fake.last_name()}',
                'size_at': fake.date_between(),
            },
        )
        for _ in range(kwargs.get('count', 10))
    ]


if __name__ == '__main__':  # pragma: no cover
    clientes = get_client_list(seed=17, lang='jp_Jp', count=15)
    print(getsizeof(clientes), getsizeof(clientes[0]))
    print(
        f'{20 * .05}',
        clientes,
    )
