# !/usr/bin/env python
# -*- coding: utf-8 -*-
from unidecode import unidecode

__author__ = "@britodfbr"  # pragma: no cover

words = [
    'missíssipi',
    'abracadabra',
    'açaí',
    'água',
]


def mapping_letters1():
    for word in words:
        print(word, unidecode(word))


def mapping_letters2():
    for word in (unidecode(w) for w in words):
        print((word))


def mapping_letters3():
    for word in (unidecode(w) for w in words):
        d = {}
        print(word, end=' ')
        for index, letter in enumerate(word):
            d.setdefault(letter, []).append(index)
        print(d)


def run():
    funcs = [
        mapping_letters1,
        mapping_letters2,
        mapping_letters3,
    ]
    for func in funcs:
        func()


if __name__ == '__main__':  # pragma: no cover
    run()
