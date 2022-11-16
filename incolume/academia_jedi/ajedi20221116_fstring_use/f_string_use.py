from math import pi
from typing import Container, Generator
from utils import description, successive_execution

number = 1000000000
n = 1_000_000_000_000
title = 'title'


@description
def example1() -> Container:
    """Uso de valores sem formatação."""
    return pi, number, n, title,


@description
def example2() -> Generator:
    """Uso de valores sem formatação no alinhamento."""
    return (f'{n}-void' for n in (7, 11, 127, 1234))


@description
def example3() -> Generator:
    """Uso de valores com formatação no alinhamento.

    f'{n:04}'  Alinhamento numérico com 4 posições.
    """
    return (f'{n:04}-void' for n in (7, 11, 137, 1234))


@description
def example4() -> (Container | Generator):
    """Uso de valores sem formatação no alinhamento para strings.
    """
    return f'{title}',


@description
def example5() -> (Container | Generator):
    """Uso de valores com formatação no alinhamento para strings.

    f'{title:<90}' alinhamento a esquerda com 90 colunas
    """
    return f'{title:<90}', f'{number}'


@description
def example6() -> (Container | Generator):
    """Uso de valores com formatação no alinhamento para strings.

    f'{title:^90}' alinhamento ao centro com 90 colunas
    """
    return f'{title:^90}', f'{n:^90}'


@description
def example7() -> (Container | Generator):
    """Uso de valores com formatação no alinhamento para strings.

    f'{title:>90}' alinhamento a esquerda com 90 colunas
    """
    return f'{title:>90}', f'{pi:>90}'


@description
def example8() -> (Container | Generator):
    """Uso de valores com formatação numérica.
    f'{n:,}' milhar
    """
    return f'{n:,}', f'{number:,}', f'{pi:,}', 100


@description
def example9() -> (Container | Generator):
    """Uso de valores com formatação numérica.
    f'{n:.0f}' decimal, onde 0 é o numero de casas.
    """
    return f'{n:.1f}', f'{number:.2f}', f'{pi:.3f}', f'{100:.4f}'


def run():
    funcs = [
        example1,
        example2,
        example3,
        example4,
        example5,
        example6,
        example7,
        example8,
        example9,
    ]
    successive_execution(funcs)


if __name__ == '__main__':  # pragma: no cover
    run()
