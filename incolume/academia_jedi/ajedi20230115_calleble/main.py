"""Module."""
# ruff: noqa: ANN002, ANN003

from collections.abc import Callable
from inspect import stack

from incolume.academia_jedi import logger


class Engine:
    """Motor."""

    def __init__(self, *args, **kwargs) -> None:
        """Init class."""
        self.args = args
        self.__dict__.update(kwargs)

    def __call__(self):
        """Call class."""
        return f'{stack()[0][3]}({self.__dict__})'


class NewEngine(Engine):
    """Novo motor."""

    def __init__(self, /, **kwargs) -> None:
        """Init class."""
        super().__init__(**kwargs)
        super().__dict__.update(kwargs)


class Gear:
    """Engrenagem."""

    def __init__(self, *args, **kwargs) -> None:
        """Init class."""
        self.args = args
        self.__dict__.update(kwargs)


def truncus(*args, **kwargs):
    """Function."""
    return f'{stack()[0][3]}({args=}, {kwargs=})'


def check_callable(func: Callable) -> bool:
    """Check calleble."""
    return callable(func)


def run():
    """Run it."""
    logger.debug(truncus(1, 2, a=1, b=2))
    n = truncus
    m = 'm'
    callables = [
        Engine(1, 2, a=1, c=4),
        truncus,
        n,
        m,
        Gear(1, b=2, c=3),
        NewEngine(a=1, b=2),
    ]
    for element in callables:
        print(
            element.__class__.__name__,
            type(element),
            check_callable(element),
            element() if check_callable(element) else None,
        )


if __name__ == '__main__':  # pragma: no cover
    run()
