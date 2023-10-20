# !/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime as dt
from dataclasses import dataclass
from typing import List


__author__ = '@britodfbr'  # pragma: no cover


@dataclass
class Message:
    tag: str
    messages: List[str]


@dataclass
class Release:
    release: str
    date: dt.datetime
    records: List[Message]


def example1():
    """Exemplo com montar os objetos."""
    print(
        Release(
            '0.1.0',
            dt.datetime.now(),
            [
                Message('Added', ['abc', 'xpto', 'khaqi']),
                Message('Changed', ['xxxxx', 'x9']),
            ],
        )
    )


def translate(tags: str):
    ...
