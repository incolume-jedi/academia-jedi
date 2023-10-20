import logging
import timeit
from typing import Callable, Optional

from truncus import brazilian_name_list

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s;%(levelname)-8s;%(name)s;'
    '%(module)s;%(funcName)s;%(message)s',
)


def tratativa1(list_names: Optional[list] = None) -> list:
    """Uppercase."""
    list_names = list_names or []
    return list(map(str.upper, list_names))


def tratativa2(list_names: Optional[list] = None) -> list:
    """Uppercase."""
    list_names = list_names or []
    return [name.upper() for name in list_names]


def get_timeit(func: Callable, listnames: list, name: str) -> float:

    speed = min(
        timeit.repeat(lambda: func(listnames), repeat=10, number=500_000),
    )
    logging.debug(f'{name:10}: {speed}"')
    return speed


def run():
    peoples = brazilian_name_list(100)
    print(peoples[0])
    print(tratativa1(peoples))
    print(tratativa2(peoples))
    get_timeit(tratativa1, peoples, name='Map')
    get_timeit(tratativa2, peoples, name='LC')


if __name__ == '__main__':  # pragma: no cover
    run()
