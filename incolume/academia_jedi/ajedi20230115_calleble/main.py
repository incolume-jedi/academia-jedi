from typing import Callable
from inspect import stack
import logging


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s;%(levelname)-8s;%(name)s;"
           "%(module)s;%(funcName)s;%(message)s",
)


class Engine:
    """Motor"""
    def __init__(self, *args, **kwargs):
        self.args = args
        self.__dict__.update(kwargs)

    def __call__(self):
        result = f'{stack()[0][3]}({self.__dict__})'
        return result


class NewEngine(Engine):
    def __init__(self, /, **kwargs):
        super().__init__(**kwargs)
        super().__dict__.update(kwargs)


class Gear:
    """Engrenagem."""
    def __init__(self, *args, **kwargs):
        self.args = args
        self.__dict__.update(kwargs)


def truncus(*args, **kwargs):
    """Function."""
    result = f'{stack()[0][3]}({args=}, {kwargs=})'
    return result


def check_calleble(func: Callable)-> bool:
    if callable(func):
        return True
    return False


def run():
    logging.debug(truncus(1, 2, a=1, b=2))
    n = truncus
    m = 'm'
    callables = [
        Engine(1, 2, a=1, c=4), truncus, n, m, Gear(1, b=2, c=3),
        NewEngine(a=1, b=2)
    ]
    for element in callables:
        print(
            element.__class__.__name__,
            type(element),
            check_calleble(element),
            element() if check_calleble(element) else None
        )


if __name__ == '__main__':    # pragma: no cover
    run()
