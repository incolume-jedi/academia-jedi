# !/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from copy import copy

from constantes import MSG, labels
import datetime as dt

__author__ = "@britodfbr"  # pragma: no cover
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s;%(levelname)-8s;%(name)s;"
           "%(module)s;%(funcName)s;%(message)s",
)


def tratativa01():
    d = {}
    # d.setdefault(letter, []).append(index)
    for i, text in enumerate(MSG.strip().split('\n')):
        print(i)
        key, value = text.split(maxsplit=1)
        print(key, value, sep='-')
        print(list(x for x in value.split('Added') if x.startswith(':')))


def tratativa02():
    for i, text in enumerate(MSG.strip().split('\n')):
        print(i, text)
        key, value = text.split(maxsplit=1)
        print(f"{key=} {value=}")
        print(type(value))
        print(value)
        tag, value = value[:value.index(':')], value[value.index(':')+1:].strip()
        print(f"{tag=} {value=}")


def tratativa03():
    """Fail loop infinito."""
    d = {}
    for i, text in enumerate(MSG.strip().split('\n')):
        logging.debug(i, text)
        key, value = text.split(maxsplit=1)
        logging.debug(f"{key=} {value=}")
        logging.debug(type(value))
        logging.debug(value)
        while value:
            try:
                tag, value = value[:value.index(':')], value[value.index(':')+1:].strip()
                print(f"{tag=} {value=}")
            except ValueError:
                pass


def tratativa04():
    msgs = MSG.strip().splitlines()
    print(msgs[-1])
    key, txt = msgs[-1].split(maxsplit=1)
    print(f'{key=} {txt=}')
    # print(txt[1:])
    d = {}
    while txt:
        try:
            word, txt = txt.split(maxsplit=1)
            print(word)
        except ValueError:
            pass


def tratativa05():
    msgs = MSG.strip().splitlines()
    print(msgs[-1])
    key, txt = msgs[-1].split(maxsplit=1)
    print(f'{key=} {txt=}')
    # print(txt[1:])
    d = {}
    while txt:
        try:
            word, txt = txt.split(maxsplit=1)
            if word in labels:
                tag = copy(word)
                d.setdefault(tag, [])
            else:
                ...
        except ValueError as e:
            print(e)
        print(d)



def translate():
    ...


def run():
    translate()
    tratativa05()


if __name__ == '__main__':    # pragma: no cover
    run()

