import logging

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
import secrets
import string
import typing

__author__ = '@britodfbr'  # pragma: no cover


def generate_password(length: int = 8):
    """"""
    length = length if length >= 8 else 8
    chars: str = string.digits + string.ascii_letters + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))


def tratativa1():
    """Return a random int in the range [0, n)."""
    return secrets.randbelow(100)


def tratativa2():
    """"""
    return secrets.choice(range(6))


def tratativa3():
    """Gerador de senhas com secrets."""
    return generate_password()


def tratativa4():
    """Numero aleatório com a quantia de bits indicada."""
    k = 2
    return secrets.randbits(k)


def tratativa5():
    """Token de bytes."""
    return secrets.token_bytes(16)


def tratativa6():
    """Token de hex."""
    return secrets.token_hex(32)


def tratativa7():
    """Token urlsafe."""
    return secrets.token_urlsafe(64)


def tratativa8():
    """"""
    return [secrets.token_urlsafe(8) for _ in range(10)]


def tratativa9():
    """Compare digest."""
    user_input, pw = '123', '123'

    return secrets.compare_digest(user_input, pw)


def tratativa10():
    """..."""
    ssr = secrets.SystemRandom()
    ssr.seed(17)
    return ssr.sample(range(1, 7), 3), ssr.choice(range(8))


def tratativa11():
    """"""


def run():
    """Running it."""
    functions: list[typing.Callable] = [
        value
        for key, value in globals().items()
        if key.__contains__('tratativa')
    ]
    for func in functions:
        logging.debug(f'{type(func)} {func.__name__}')
        print(f'--- {func.__name__} ---')
        print(f'    >>> {func.__doc__}')
        try:
            if result := func():
                print(result)
        except ValueError as e:
            logging.exception(f'{e.__class__.__name__}: {e}')
        finally:
            logging.debug(f'{func.__name__} finished.')
        print('------\n')


if __name__ == '__main__':  # pragma: no cover
    run()
