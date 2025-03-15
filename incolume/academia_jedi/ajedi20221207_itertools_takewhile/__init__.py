"""EStudo takewhile."""
# ruff: noqa: T201

from collections.abc import Container
from itertools import takewhile

numbers = [1, 2, 3, -1, 3, 2, 1]


def without_takewhile(numbers: Container) -> None:
    """Without takewhile."""
    for number in numbers:
        if number <= 0:
            break
        print(number)


def with_takewhile(numbers: Container) -> None:
    """With takewhile."""
    items = takewhile(lambda x: x >= 0, numbers)
    for item in items:
        print(item)
