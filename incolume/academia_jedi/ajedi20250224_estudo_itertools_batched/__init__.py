"""Module for studing itertools.batched."""

from collections.abc import Iterable
from itertools import batched

length = 10
data = list(range(length))


def running(array: Iterable, length: int = 0) -> list:
    """Applied study."""
    return list(batched(array, length))


def run():
    """Run it."""
