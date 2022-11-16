__author__ = "@britodfbr"  # pragma: no cover

from functools import wraps
from typing import Callable, Any


def successive_execution(funcs: Any):
    for i, func in enumerate(funcs):
        # print(type(func))
        func()
    ...


def description(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print(
            '=' * 90,
            f'{func.__name__:^90}',
            f'{func.__doc__}',
            '-' * 90,
            *func(*args, **kwargs),
            '---' * 30,
            '',
            sep='\n'
        )

    return inner
