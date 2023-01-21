import random
from functools import lru_cache
from itertools import zip_longest
from collections import Counter

__author__ = "@britodfbr"  # pragma: no cover
random.seed(17)

l = [random.randint(1, 10) for _ in range(100)]


def with_builtins():
    print(
        l, max(l), set(l), l.count(9), max(l, key=l.count), sep="\n"  # Moda encontrada
    )


def with_collections():
    c = Counter(l)

    print(
        l,
        c,
        c.most_common(3),  # 3 maiores ocorrencias
        c.values(),
        c.keys(),
        c.items(),
        list(c.elements()),
        c.total(),
        c.most_common(1),  # moda
        sep="\n",
    )


def run():
    functions = [
        with_builtins,
        with_collections,
    ]

    for func in functions:
        print(f"{func.__name__.upper()}".center(90))
        func()
        print("---" * 30)


if __name__ == "__main__":  # pragma: no cover
    run()
