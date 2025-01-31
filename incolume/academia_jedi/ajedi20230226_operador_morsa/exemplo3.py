"""Module.

Unificados a partir dos arquivos oriundos de
incolume/academia_jedi/ajedi20221106_operador_morsa/.
"""

import logging
from enum import Enum, auto

import easygui as eg
from icecream import ic

__author__ = '@britodfbr'  # pragma: no cover


def gretting(username: str = '') -> str:
    """Gretting."""
    if name := username or 'world':
        return f'Hello {name.title()}!'
    return 'Hello guest.'


class Viewer(Enum):
    """Viewer class."""

    CLI = auto()
    EASYGUI = auto()

    def __call__(self, **kwargs):
        """Call it."""
        logging.debug(self.__dict__)
        logging.debug(self.name)
        msg = kwargs.get('msg')
        title = kwargs.get('title', 'App')
        default = kwargs.get('default', '')
        match self.name:
            case 'CLI':
                return gretting(input(f'{msg} '))
            case 'EASYGUI':
                return gretting(
                    eg.enterbox(msg=f'{msg} ', title=title, default=default),
                )
            case _:
                raise NotImplementedError


def viewer():
    """Viewer."""
    return Viewer.EASYGUI(name='')


def run():
    """Run it."""
    ic(Viewer.CLI(msg='What is your name?'))
    ic(Viewer.EASYGUI(msg='What is your name?'))
    ic(Viewer.EASYGUI(msg='What is your name?', title='Get username'))


if __name__ == '__main__':  # pragma: no cover
    run()
