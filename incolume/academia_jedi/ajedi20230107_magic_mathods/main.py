from random import random, seed

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
from currency import NC, Currency
from real import Real

__author__ = '@britodfbr'  # pragma: no cover


def run():
    seed(23)
    r = Real(0.2)
    p = Real(1)
    print(r)
    print(r + p)
    print(r > p)
    print(r < p)
    print(sorted((r, p), reverse=True))

    q = [Currency(random()) for _ in range(10)]
    s = [Currency(random(), symbol='$', sigla='USD') for _ in range(10)]
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
    print(9, t - Currency(0.12))
    print(10, Currency(0.12) - t)
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
