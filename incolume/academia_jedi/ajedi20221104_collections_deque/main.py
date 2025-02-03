"""Collections deque.


https://docs.python.org/3/library/collections.html#collections.deque
"""

import itertools

# !/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import deque
from collections.abc import Iterator
from pathlib import Path

__author__ = '@britodfbr'  # pragma: no cover

# ruff: noqa: 201
# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293


def example1():
    d = deque('ghi')  # make a new deque with three items
    for elem in d:  # iterate over the deque's elements
        print(elem.upper())

    d.append('j')  # add a new entry to the right side
    d.appendleft('f')  # add a new entry to the left side
    print(d)  # show the representation of the deque

    print(
        d.pop(),  # return and remove the rightmost item 'j'
        d.popleft(),  # return and remove the leftmost item 'f'
        list(d),  # list the contents of the deque ['g', 'h', 'i']
        d[0],  # peek at leftmost item 'g'
        d[-1],  # peek at rightmost item 'i'
        list(reversed(d)),
        # list the contents of a deque in reverse ['i', 'h', 'g']
        'h' in d,  # search the deque True
        d.extend('jkl'),  # add multiple elements at once d
        deque(['g', 'h', 'i', 'j', 'k', 'l']),
        d.rotate(1),  # right rotation  d
        deque(['l', 'g', 'h', 'i', 'j', 'k']),
        d.rotate(-1),  # left rotation d
        deque(['g', 'h', 'i', 'j', 'k', 'l']),
        deque(reversed(d)),  # make a new deque in reverse order
        deque(['l', 'k', 'j', 'i', 'h', 'g']),
        d.clear(),  # empty the deque
        d.extendleft('abc'),  # extendleft() reverses the input order d
        deque(['c', 'b', 'a']),
        sep='\n',
    )


def example2():
    """Access file."""
    file = Path(__file__).parents[3] / 'data_files' / 'proxies_1663514130.csv'

    def tail(filename, n=10):
        """Return the last n lines of a file."""
        with open(filename) as f:
            return deque(f, n)

    print(tail(file, 3))


def example3():
    """Média móvel."""

    def moving_average(iterable, n=3):
        # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
        # https://en.wikipedia.org/wiki/Moving_average
        it = iter(iterable)
        d = deque(itertools.islice(it, n - 1))
        d.appendleft(0)
        s = sum(d)
        for elem in it:
            s += elem - d.popleft()
            d.append(elem)
            yield s / n

    mm = moving_average([4, 3, 5, 4, 3, 4])
    print([next(mm) for _ in range(4)])


def example4():
    def roundrobin(*iterables):
        """roundrobin('ABC', 'D', 'EF') --> A D E B F C."""
        iterators = deque(map(iter, iterables))
        while iterators:
            try:
                while True:
                    yield next(iterators[0])
                    iterators.rotate(-1)
            except StopIteration:
                # Remove an exhausted iterator.
                iterators.popleft()

    rr = roundrobin('ABCD', 'EF', 'GHI')

    print([next(rr) for _ in range(9)])


def example5():
    """Deletar Nezimo termo."""
    l = ['A', 'E', 'G', 'B', 'F', 'H', 'C', 'I', 'D']

    def delete_nth(d: Iterator, n: int = 0):
        d = deque(d)
        d.rotate(-n)
        d.popleft()
        d.rotate(n)
        return d

    print(l, delete_nth(l, -1))
    print(l, delete_nth(l, 2))


def run():
    functions = [
        example1,
        example2,
        example3,
        example4,
        example5,
    ]

    for func in functions:
        print('===' * 30)
        print(f'{func.__name__.upper()}'.center(90))
        print(f'{func.__doc__}'.center(90))
        print('---' * 30)
        func()
        print('---' * 30)


if __name__ == '__main__':
    run()
