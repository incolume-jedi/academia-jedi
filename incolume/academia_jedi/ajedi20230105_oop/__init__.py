"""Estudos sobre Programação Orientada a Objetos."""

import random

from icecream import ic
from incolume.academia_jedi.ajedi20230105_oop import frutas, interface


def run():
    """Run it."""
    fruta = interface.Fruta(nome='Manga espada')
    manga = frutas.Manga(0.2)
    ic(fruta)
    ic(isinstance(manga, interface.Fruta), manga)

    uva = frutas.Uva(1)
    ic(isinstance(uva, interface.Fruta), uva)

    pontos = [
        interface.Point(random.randint(0, 5), random.randint(0, 5))  # noqa: S311
        for _ in range(5)
    ]
    ic(pontos)
    ic(f'{pontos[0]}')


if __name__ == '__main__':
    run()
