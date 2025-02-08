# !/usr/bin/env python

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
__author__ = '@britodfbr'  # pragma: no cover

import re
from collections import namedtuple

User = namedtuple('User', 'name zipcode fone celfone email pw')
u1 = User(
    'Ricardo Brito do Nascimento',
    '72.000-000',
    '3535-3535',
    '93535-3535',
    'jesus@example.com',
    'a1B@§',
)


def show():
    regex = r'^[A-Z]+$'
    pattern = re.compile(regex, flags=re.I)
    print(
        pattern.search('HELLO'),
        pattern.search('HELLO WORLD'),
        pattern.search('Hello World'),
        pattern.search('hello world'),
        pattern.search('helloworld'),
        pattern.match('helloworld'),
        pattern.match('hello world'),
        pattern.fullmatch('hello world'),
        sep='\n',
    )


def example1(entrada: str) -> str:
    """Validação nome completo."""
    pat = re.compile(r'^(\w+\s)+\w+$', flags=re.I)
    result = pat.search(entrada)
    return pat.search(entrada).string if result else ''


def example2(entrada: str):
    """Validação CEP brasileiro."""
    pat = re.compile(r'^[78]\d\.?\d{3}-\d{3}$')
    return pat.match(entrada)


def example3(entrada: str):
    """Validação de telefone fixo."""
    pat = re.compile(r'^[1-6]\d{3}-?\d{4}$')
    return pat.match(entrada)


def example4(entrada: str):
    """Validação de telefone celular."""
    pat = re.compile(r'^[7-9]\d{4}-?\d{4}$')
    return pat.match(entrada)


def example5(entrada: str):
    """Validação de email."""
    pat = re.compile(
        r'^([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+$',
    )
    return pat.match(entrada)


def run():
    show()
    print('-' * 20)
    print(
        example1(u1.name),
        example2(u1.zipcode),
        example3(u1.fone),
        example4(u1.celfone),
        example5(u1.email),
        sep='\n',
    )


if __name__ == '__main__':  # pragma: no cover
    run()
