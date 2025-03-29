"""Estudos com lru_cache implementações."""

from collections.abc import Generator
from functools import lru_cache

__author__ = '@britodfbr'  # pragma: no cover


def fibonacci0() -> Generator:
    """Fibonacci.

    Yields:
        Generator: _description_
    """
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


def fibonacci1(n: int) -> Generator:
    """Fibonacci."""
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


@lru_cache
def fibonacci2(n: int) -> Generator:
    """Fibonacci."""
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
