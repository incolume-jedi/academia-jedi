"""Module.

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

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
