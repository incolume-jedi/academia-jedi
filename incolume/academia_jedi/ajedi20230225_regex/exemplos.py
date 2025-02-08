"""Module ..."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

import inspect
import logging
import re
import typing
from dataclasses import dataclass, field

from incolume.academia_jedi.ajedi20220928_regex.app import (
    example1,
    example2,
    example3,
    example4,
    example5,
    show,
)

__author__ = '@britodfbr'  # pragma: no cover

GRETTINS: typing.Final[list[str]] = [
    'HELLO',
    'HELLO WORLD',
    'Hello World',
    'hello world',
    'Helloworld',
    'helloworld',
    'hello world',
    'HELLO world',
    'hello WORLD',
]


@dataclass
class User:
    name: str
    cpf: str
    zipcode: str
    fone: str
    celfone: str
    email: str
    pw: str = field(repr=False)
    ccredit: str = field(default='', repr=False)


user = User(
    'Ricardo Brito do Nascimento',
    '000.000.001-91',
    '72.000-000',
    '3535-3535',
    '93535-3535',
    'jesus@example.com',
    'a1B@§',
)


def example6(entrada: str) -> bool:
    """Validação nome completo."""
    pat = re.compile(r'^(\w+\s)+\w+$', flags=re.I)
    return bool(pat.search(entrada))


def example7(entrada: str) -> bool:
    """Validação CEP brasileiro."""
    pat = re.compile(r'^[78]\d\.?\d{3}-\d{3}$')
    return bool(pat.match(entrada))


def example8(entrada: str, regex: str = '') -> bool:
    """Validação de senhas.

    Deve conter pelo menos uma letra minúscula
    Deve conter pelo menos uma letra maiúscula
    Deve conter pelo menos um número
    Deve conter pelo menos um caractere especial
       (por exemplo, !, @, #, $, %, ^, &, *, (, ), -,
    """
    regex = (
        regex
        or r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    )
    pat: re.Pattern = re.compile(regex)
    return bool(pat.match(entrada))


def example9(entrada: str, regex: str = '') -> bool:
    """Validação do número de cartão de crédito."""
    regex = (
        regex
        or '^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|'
        '6(?:011|5[0-9]{2})[0-9]{12}|3[47][0-9]{13})$'
    )
    pat: re.Pattern = re.compile(regex)
    return bool(pat.match(entrada))


def tratativa0():
    """Tratativa em capturar a docstring."""
    logging.debug(
        f'>>> {inspect.stack()[0][3]} {inspect.currentframe().f_code.co_name}',
    )
    print(f'{locals()=}')
    print(f'{globals()=}')
    print(
        f'>>> {inspect.stack()[0][3]} {inspect.currentframe().f_code.co_name}',
    )
    print(f'>>> {globals().get(inspect.stack()[0][3]).__doc__}\n')


def tratativa1():
    """Reescrita do metodo app.show."""
    print(f'>>> {globals().get(inspect.stack()[0][3]).__doc__}\n')
    regex = r'^[A-Z]+$'
    pattern = re.compile(regex, flags=re.I)
    show()  # app.show
    print('=======')
    for term in GRETTINS:
        logging.debug(f'{regex=} {term=}')
        print(f'-- search -- {term}, {pattern.search(term)}')
        print(f'-- match -- {term}, {pattern.match(term)}')
        print(f'-- fullmatch -- {term}, {pattern.fullmatch(term)}')


def tratativa2():
    """Validação de nome completo."""
    print(f'>>> {globals().get(inspect.stack()[0][3]).__doc__}')
    print(f'{example1(user.name)=}')
    print(f"{example1('josé')=}")
    print(f"{example1('José')=}")
    print(f'{example6(user.name)=}')
    print(f"{example6('josé')=}")
    print(f"{example6('José')=}")


def tratativa3():
    """Validação de CEP Brasileiro."""
    print(f'>>> {globals().get(inspect.stack()[0][3]).__doc__}\n')
    print(f'{example2(user.zipcode)=}')
    print(f'{example7(user.zipcode)=}')


def tratativa4():
    """Validação de telefone fixo."""
    print(f'>>> {globals().get(inspect.stack()[0][3]).__doc__}\n')
    print(f'{example3(user.fone)=}')
    print(f'{example3(user.celfone)=}')


def tratativa5():
    """Validação de telefone celular."""
    print(f'>>> {globals().get(inspect.stack()[0][3]).__doc__}\n')
    print(f'{example4(user.fone)=}')
    print(f'{example4(user.celfone)=}')


def tratativa6():
    """Validação de endereço de email."""
    print(f'>>> {globals().get(inspect.stack()[0][3]).__doc__}\n')
    print(f'{example5(user.email)}')
    print(f'{example5("jc21@exemplo.org")}')
    print(f'{example5("jc-33@exemplo.org")}')


def tratativa7():
    """Validação de senhas.

    Deve conter pelo menos 2 letra minúscula
    Deve conter pelo menos 2 letra maiúscula
    Deve conter pelo menos 2 número
    Deve conter pelo menos 2 caractere especial
    """
    print(f'>>> {globals().get(inspect.stack()[0][3]).__doc__}\n')
    regex = r'^(?=(?:.*[a-z]){2})(?=(?:.*[A-Z]){2})(?=(?:.*\d){2})(?=(?:.*[@$!%*?&]){2})[A-Za-z\d@$!%*?&]{8,}$'

    print(f'{user.pw=} {example8(user.pw)=}')
    print(f'{user.pw=} {example8(user.pw, regex)=}')
    senha = 'Ab12!@Ba'
    print(f'{senha=}{example8(senha)=}')
    print(f'{senha=}{example8(senha, regex)=}')


def tratativa8():
    """Validação do nº de cartão de crédito."""
    print(f'>>> {globals().get(inspect.stack()[0][3]).__doc__}\n')
    logging.debug(user)
    card_numbers = (
        '4392 6716 3103 0794',
        '5549 2760 1670 0646',
    )
    print(f'{user.ccredit=} {example9(user.ccredit)=}')
    for num in card_numbers:
        m = re.sub(r'\s', '', num)
        print(f'{num=} {example9(m)}')


def run():
    """Run this module."""
    functions: typing.Generator[typing.Callable] = (
        value
        for key, value in globals().items()
        if key.startswith('tratativa')
    )
    for func in functions:
        logging.debug(f'{type(func)} {func.__name__}')
        print(f'--- {func.__name__} ---')
        try:
            func()
        except ValueError as e:
            logging.exception(f'{e.__class__.__name__}: {e}')
        print('---=---\n')


if __name__ == '__main__':  # pragma: no cover
    run()
