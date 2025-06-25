"""Module."""

import timeit
from collections.abc import Callable

from incolume.academia_jedi import logger
from incolume.academia_jedi.ajedi20230115_pythonic.truncus import (
    brazilian_name_list,
)


def tratativa1(list_names: list | None = None) -> list:
    """Uppercase."""
    list_names = list_names or []
    return list(map(str.upper, list_names))


def tratativa2(list_names: list | None = None) -> list:
    """Uppercase."""
    list_names = list_names or []
    return [name.upper() for name in list_names]


def get_timeit(func: Callable, listnames: list, name: str) -> float:
    """Get timeit."""
    speed = min(
        timeit.repeat(lambda: func(listnames), repeat=10, number=500_000),
    )
    logger.debug(f'{name:10}: {speed}"')
    return speed


def run():
    """Run it."""
    peoples = brazilian_name_list(100)
    print(peoples[0])
    print(tratativa1(peoples))
    print(tratativa2(peoples))
    print(
        get_timeit(tratativa1, peoples, name='Map'),
        get_timeit(tratativa2, peoples, name='LC'),
        sep='\n',
    )


if __name__ == '__main__':  # pragma: no cover
    run()
