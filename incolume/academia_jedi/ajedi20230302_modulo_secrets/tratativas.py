import logging
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
