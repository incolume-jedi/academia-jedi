from functools import lru_cache

__author__ = "@britodfbr"  # pragma: no cover


def fibonacci0():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


def fibonacci1(n: int):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


@lru_cache()
def fibonacci2(n: int):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
