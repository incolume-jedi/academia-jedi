from real import Real
from currency import Currency, NC
from random import seed, random

__author__ = "@britodfbr"  # pragma: no cover


def run():
    seed(23)
    r = Real(.2)
    p = Real(1)
    print(r)
    print(r + p)
    print(r > p)
    print(r < p)
    print(sorted((r, p), reverse=True))

    q = list(Currency(random()) for _ in range(10))
    s = list(Currency(random(), symbol='$', sigla='USD') for _ in range(10))
    print(q, s)

    print(Currency(10) + Currency(12))
    print(sorted(s))
    print(sorted(q, reverse=True))
    t = Currency(12.34)
    t += Currency(11.11)
    print(t)
    t -= Currency(22.22)
    print(1, t)
    print(2, t + Currency(1))
    print(3, t * 3)
    print(4, 2 * t)
    print(5, t + 1)
    print(6, 1 + t)
    print(7, 1 - t)
    print(8, t - 1)
    print(9, t - Currency(.12))
    print(10, Currency(.12) - t)
    print(t // 2)
    print(2 // t)
    print(Currency(120) // t)
    print(t / 2)
    m = [NC(random()) for _ in range(5)]
    print(m)
    print(sorted(m))
    print(sorted(m, reverse=True))
    n = NC(1)
    print(n)


if __name__ == '__main__':  # pragma: no cover
    run()
