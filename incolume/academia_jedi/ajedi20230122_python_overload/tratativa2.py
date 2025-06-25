"""Exemplo singledispatchmethod."""

# ruff: noqa: ANN002, ANN003, ANN202, D101, D102, D107, FBT001, PYI041, TRY002

import platform
import sys
from dataclasses import dataclass
from functools import singledispatchmethod

from incolume.academia_jedi import logger

__author__ = '@britodfbr'  # pragma: no cover

if sys.version_info < (3, 11):
    msg = f'Incompatible python version. Current {platform.python_version()}. minimal Python 3.11+'
    raise Exception(
        msg,
    )


@dataclass
class HandlerReverse:
    def __init__(self, *args, **kwargs) -> None:
        logger.debug(f'Class {self.__class__.__name__} inited..')
        super().__init__(*args, **kwargs)

    @singledispatchmethod
    def reverse(self, value):
        msg = 'Not Implemented ..'
        logger.info(f'{value=}; {type(value)=}')
        raise NotImplementedError(msg)

    @reverse.register
    def _(self, value: (int | float)):
        logger.info(f'{value=}; {type(value)=}')
        return -value

    @reverse.register
    def _(self, value: bool):
        logger.info(f'{value=}; {type(value)=}')
        return not value

    @reverse.register
    def _(self, value: (str | list)):
        logger.info(f'{value=}; {type(value)=}')
        return value[::-1]
