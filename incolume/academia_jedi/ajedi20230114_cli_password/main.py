"""Estudos com pwinput e ofuscação de senhas."""

# ruff: noqa: UP036

import contextlib
import sys

if sys.version_info < (3, 10):
    import pwinput
else:
    with contextlib.suppress(SystemExit):
        sys.exit('This application need Python 3.10+')


def get_pwd(msg: str = '') -> str:
    """Get password."""
    msg = msg or 'Informe tua senha: '
    return input(msg)


def get_pwd_ofuscated(msg: str = '') -> str:
    """Get password ofuscated."""
    msg = msg or 'Informe tua senha: '
    return pwinput.pwinput(msg, mask='*')


def run():
    """Run it."""
    print(get_pwd())
    print(get_pwd_ofuscated())


if __name__ == '__main__':  # pragma: no cover
    run()
