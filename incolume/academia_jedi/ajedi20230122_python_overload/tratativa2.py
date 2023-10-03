"""Exemplo singledispatchmethod."""

import logging
import platform
import sys
from functools import singledispatchmethod
from dataclasses import dataclass

__author__ = '@britodfbr'  # pragma: no cover

if sys.version_info < (3, 11):
    raise Exception(
        f'Incompatible python version. Current {platform.python_version()}.'
        f' minimal Python 3.11+'
    )


@dataclass
class HandlerReverse:
    def __init__(self, *args, **kwargs):
        logging.debug(f'Class {self.__class__.__name__} inited..')
        super().__init__(*args, **kwargs)

    @singledispatchmethod
    def reverse(self, value):
        raise NotImplementedError('Not Implemented ..')

    @reverse.register
    def _(self, value: (int | float)):
        logging.info(f'{value=}; {type(value)=}')
        return -value

    @reverse.register
    def _(self, value: bool):
        logging.info(f'{value=}; {type(value)=}')
        return not value

    @reverse.register
    def _(self, value: (str | list)):
        logging.info(f'{value=}; {type(value)=}')
        return value[::-1]
