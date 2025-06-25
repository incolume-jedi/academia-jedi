"""Module principal."""

import secrets

from config import settings
from icecream import ic

ic.disable()
if settings.debug_mode:
    ic.enable()


def jogo(tries: int = 3) -> None:
    """Jogo.

    Args:
        tries (int, optional): _description_. Defaults to 3.
    """
    number: int = secrets.randbelow(3)
    for _ in range(tries):
        if (
            my_num := int(input('Dê um palpite e tente adivinhar o número: '))
        ) == number:
            ic(my_num, number)
            print('parabéns você acertou!!!')
            break
        if my_num < number:
            ic(my_num, number)
            print('O número é maior que o palpite')
        elif my_num > number:
            ic(my_num, number)
            print('O número é menor que o palpite')
