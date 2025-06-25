"""EStudo sobre listcomprehentions."""

from config import settings
from icecream import ic

# ruff: noqa: PERF401

ic.disable()
if settings.debug_mode:
    ic.enable()

valores: list[int] = [30, 50, 100, 120]
palavras: list[str] = [
    'tests',
    'IMPLEMENTAÇÃO',
    'do',
    'TDD',
    'Para Get Connection',
]


def generate_triplo(entrada: list[int]) -> None:
    """Gerador de triplo.

    Sem listcomprehention.
    """
    triplos = []
    for valor in entrada:
        triplos.append(valor * 3)
    print(triplos)


def gen_multiple(entrance: list[int], fator: int = 3) -> None:
    """Gerador multiplos com listcomprehention."""
    fator = fator if fator > 1 else 2
    print([valor * fator for valor in entrance])


def gen_letter_count(entrance: list[str]) -> dict[str, int]:
    """Gerador de contador de letras."""
    return {world.casefold(): len(world) for world in entrance}


def problema_conjunto() -> set:
    """Problema sobre conjunto.

    Utilizando operações de conjunto encontre o grupo de amigos que gostam de
    programar, fezem curso on-line de programação,
    mas não gostam de jogar futebol.
    Gostam de programação: Ricardo, Roberto, Ana, Gustavo, Vinicius
    gostam de futebol: Ada, Roberto, Mateus, Vinicius, Paulo
    curso de programação on-line: Ricardo, Mateus, Paulo, Pedro
    """
    gostam_prog = 'Ricardo Roberto Ana Gustavo Vinicius'
    gostam_fut = 'Ada Roberto Mateus Vinicius Paulo'
    estudo_online = 'Ricardo Mateus Paulo Pedro'

    return (
        set(gostam_prog.split())
        .intersection(estudo_online.split())
        .difference(gostam_fut.split())
    )


def problem_set() -> set:
    """Segunda solução."""
    l1 = ['Ricardo', 'Roberto', 'Ana', 'Gustavo', 'Vinicius']
    l2 = ['Ada', 'Roberto', 'Mateus', 'Vinicius', 'Paulo']
    l3 = ['Ricardo', 'Mateus', 'Paulo', 'Pedro']
    gostam_prog = set(l1)
    gostam_fut = set(l2)
    estudo_online = set(l3)
    return (gostam_prog | estudo_online) - gostam_fut
