"""Module for studing itertools.batched."""

import itertools
from collections.abc import Iterable

length = 10
data = list(range(length))


def running(array: Iterable, length: int = 0) -> list:
    """Applied study."""
    return list(itertools.batched(array, length))


def run():
    """Run it."""
