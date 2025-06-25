# !/usr/bin/env python

# ruff: noqa: ANN201, D100, D101, DTZ005
import datetime as dt
from dataclasses import dataclass

from icecream import ic
from incolume.academia_jedi import logger

__author__ = '@britodfbr'  # pragma: no cover


@dataclass
class Message:
    tag: str
    messages: list[str]


@dataclass
class Release:
    release: str
    date: dt.datetime
    records: list[Message]


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
        ),
    )


def translate(tags: str):
    """Translate tags to Portuguese."""
    logger.debug(ic(tags))
