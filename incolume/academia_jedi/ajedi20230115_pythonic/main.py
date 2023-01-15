import timeit
from typing import Callable

from truncus import brazilian_name_list
import logging


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s;%(levelname)-8s;%(name)s;"
           "%(module)s;%(funcName)s;%(message)s",
)


def tratativa1(list_names: list = None) -> list:
    """Uppercase."""
    list_names = list_names or []
    result = list(map(str.upper, list_names))
    return result


def tratativa2(list_names: list = None) -> list:
    """Uppercase."""
    list_names = list_names or []
    result = [name.upper() for name in list_names]
    return result


def get_timeit(func: Callable, listnames: list, name: str) -> float:

    speed = min(
        timeit.repeat(lambda: func(listnames), repeat=10, number=500_000))
    logging.debug(f"{name:10}: {speed}\"")
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
