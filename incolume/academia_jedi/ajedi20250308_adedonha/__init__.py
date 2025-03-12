"""Submodule."""

from __future__ import annotations

import logging
from string import ascii_uppercase

from icecream import ic


# ruuf: noqa: ERA001
def adedonha(num: int | str = 0) -> str:
    """Jogo adedonha.

    Args:
        num (int): Numero de entrada.

    Returns:
        str: letra selecionada.
    """
    try:
        if type(num) not in (int, str) or not num:
            raise AssertionError  # noqa: TRY301
        num = int(num)
    except (AssertionError, ValueError) as err:
        msg = 'num only numeric values'
        # logging.exception(ic(msg))  # noqa: ERA001
        ic(msg)
        raise TypeError(msg) from err

    index = num % len(ascii_uppercase)
    logging.debug(ic(index))
    return ascii_uppercase[index - 1]
