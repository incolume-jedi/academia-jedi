"""Operador examples."""

from functools import reduce
from operator import add, floordiv, itemgetter, mod, mul, sub
from pprint import pprint

nums = list(range(1, 11))
words = ['editor', 'amar', 'zebra', 'falar', 'acreditar', 'grunir', 'abraço']


def exemplo01(numbers: list | None = None) -> tuple:
    """Reduce with operator."""
    numbers = numbers or nums
    return (
        [
            # Sem operator
            reduce(lambda x, y: x + y, numbers),
            reduce(lambda x, y: x - y, numbers),
            reduce(lambda x, y: x * y, numbers),
            reduce(lambda x, y: x % y, numbers),
        ],
        [
            # Com operator
            reduce(add, nums),
            reduce(sub, nums),
            reduce(mul, nums),
            reduce(mod, nums),
        ],
    )


def exemplo02() -> tuple:
    """Ordenar pelo segundo caracter."""
    return (
        sorted(words, key=lambda palavra: palavra[1]),
        sorted(words, key=itemgetter(1)),
    )


def exemplo03() -> None:
    """Novo exemplo."""
    print(  # noqa: T201
        reduce(floordiv, sorted(nums, reverse=True)),
        end='\n',
    )


def run() -> None:
    """Run it."""
    for func in (f for n, f in globals().items() if n.startswith('exemplo')):
        print(  # noqa: T201
            '====',
            f'{func.__name__} - {func.__doc__}',
            '---',
            end='\n',
        )
        pprint(func())  # noqa: T203
        print('---')  # noqa: T201


if __name__ == '__main__':  # pragma: no cover
    run()
