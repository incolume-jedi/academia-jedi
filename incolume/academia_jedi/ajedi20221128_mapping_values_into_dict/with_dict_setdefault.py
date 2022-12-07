# !/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import re
import subprocess
from copy import copy
from dataclasses import dataclass
from typing import Any

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
        tag, value = (
            value[:value.index(':')],
            value[value.index(':') + 1:].strip()
        )
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
                tag, value = (
                    value[:value.index(':')],
                    value[value.index(':') + 1:].strip()
                )
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


def tratativa06():
    ...


def tratativa07():
    msg = MSG.strip().splitlines()[-1]
    logging.debug(f"{msg=}")
    key, msg = msg.split(maxsplit=1)
    logging.debug(f"{key=}")
    logging.debug(f"{msg=}")
    txt = re.sub(
        "(Added|Changed|Deprecated|Removed|Fixed|Security):",
        "§\\1:",
        msg,
        flags=re.I
    )
    logging.debug(f"{txt=}")
    logging.debug(txt.strip().split('§'))
    logging.debug(list(x.strip() for x in txt.strip().split('§') if x))
    dct = {}
    for i, j in (x.strip().split(':') for x in txt.strip().split('§') if x):
        logging.debug(f"{i=} {j=}")
        dct.setdefault(i, []).extend(j.strip().split(';'))
    logging.debug(dct)
    # values = dct.values()
    # logging.debug(f"{values=}")
    for x, y in dct.items():
        # print(x, y)
        dct[x] = [a for a in y if a]
    logging.debug(dct)
    ...


def tratativa08():
    msg = MSG.strip().splitlines()[-1]
    logging.debug(f"{msg=}")
    key, msg = msg.split(maxsplit=1)
    logging.debug(f"{key=}")
    logging.debug(f"{msg=}")
    txt = re.sub(
        "(Added|Changed|Deprecated|Removed|Fixed|Security):",
        r"§\1:",
        msg,
        flags=re.I
    )
    logging.debug(f"{txt=}")
    logging.debug(txt.strip().split('§'))
    logging.debug(list(x.strip() for x in txt.strip().split('§') if x))
    dct = {}
    for i, j in (x.strip().split(':') for x in txt.strip().split('§') if x):
        logging.debug(f"{i=} {j=}")
        dct.setdefault(i, []).extend(j.strip().split(';'))
    logging.debug(dct)
    # values = dct.values()
    # logging.debug(f"{values=}")
    for x, y in dct.items():
        # print(x, y)
        dct[x] = [a for a in y if a]
    logging.debug(dct)
    result = {'key': key, 'date': dt.datetime.now(), 'messages': dct}
    logging.debug(result)
    return result


def tratativa09():
    def msg_classify(msg: str) -> dict:
        key, msg = msg.split(maxsplit=1)
        txt = re.sub(
            "(Added|Changed|Deprecated|Removed|Fixed|Security):",
            r"§\1:",
            msg,
            flags=re.I
        )
        dct = {}
        for i, j in (
            x.strip().split(':') for x in txt.strip().split('§') if x
        ):
            logging.debug(f"{i=} {j=}")
            dct.setdefault(i, []).extend(j.strip().split(';'))
        for x, y in dct.items():
            dct[x] = [a for a in y if a]

        result = {'key': key, 'date': dt.datetime.now(), 'messages': dct}
        return result

    def changelog_messages(text: str) -> list:
        result = []
        for msg in text.strip().splitlines()[:]:
            result.append(msg_classify(msg))
        return result

    print(changelog_messages(MSG))


def tratativa10():
    def msg_classify(msg: str) -> dict:
        key, msg = msg.split(maxsplit=1)
        txt = re.sub(
            "(Added|Changed|Deprecated|Removed|Fixed|Security):",
            r"§\1:",
            msg,
            flags=re.I
        )
        dct = {}
        for i, j in (
            x.rstrip().rstrip(';').split(':')
            for x in txt.strip().split('§') if x
        ):
            dct.setdefault(i, []).extend(j.strip().split(';'))

        result = {'key': key, 'date': dt.datetime.now(), 'messages': dct}
        return result

    def changelog_messages(
        *, text: str, start: Any = None, end: Any = None) -> list:
        result = []
        for msg in text.strip().splitlines()[start:end]:
            result.append(msg_classify(msg))
        return result

    print(changelog_messages(text=MSG, start=10, end=20))


def tratativa11():
    class ChangeLog:
        def __init__(self):
            self.messages = []

        def __msg_classify(self, msg) -> dict:
            key, msg = msg.split(maxsplit=1)
            txt = re.sub(
                "(Added|Changed|Deprecated|Removed|Fixed|Security):",
                r"§\1:",
                msg,
                flags=re.I
            )
            dct = {}
            for i, j in (
                x.rstrip().rstrip(';').split(':')
                for x in txt.strip().split('§') if x
            ):
                dct.setdefault(i, []).extend(j.strip().split(';'))

            result = {'key': key, 'date': dt.datetime.now(), 'messages': dct}
            return result

        def messages_update(
              self, *, start: Any = None, end: Any = None) -> list:
            text = subprocess.getoutput('git tag -n')
            result = []
            for msg in text.strip().splitlines()[start:end]:
                result.append(self.__msg_classify(msg))
            self.messages = result
            return self.messages

    print(ChangeLog().messages)


def translate():
    ...


def run():
    translate()
    tratativa11()


if __name__ == '__main__':  # pragma: no cover
    run()
