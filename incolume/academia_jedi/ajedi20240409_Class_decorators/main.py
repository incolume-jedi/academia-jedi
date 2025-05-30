"""Class decorators module."""

from decorator import Accolade
from icecream import ic
from propertly import Pencil


@Accolade
def simple_function(name: str) -> None:
    """Simple function."""
    ic(name)


def run():
    """Run it."""
    simple_function('John McKinsey')

    hb = Pencil(100)
    ic(hb.counter)
    hb.counter = 20
    ic(hb.counter)


if __name__ == '__main__':
    run()
