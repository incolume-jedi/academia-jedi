from collections.abc import Container, Generator

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
from dataclasses import dataclass
from datetime import datetime
from math import pi

from utils import description, successive_execution

number = 1000000000
n = 1_000_000_000_000
title = 'title'


@dataclass
class User:
    name: str
    born: datetime

    def __str__(self) -> str:
        return (
            f'{self.__class__.__name__}'
            f'({self.name=}, {self.born=:%FT%T.%f})'
        )


@description
def example1() -> Container:
    """Uso de valores sem formatação."""
    return (
        pi,
        number,
        n,
        title,
    )


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
def example4() -> Container | Generator:
    """Uso de valores sem formatação no alinhamento para strings."""
    return (f'{title}',)


@description
def example5() -> Container | Generator:
    """Uso de valores com formatação no alinhamento para strings.

    f'{title:<90}' alinhamento a esquerda com 90 colunas
    """
    return f'{title:<90}', f'{number}'


@description
def example6() -> Container | Generator:
    """Uso de valores com formatação no alinhamento para strings.

    f'{title:^90}' alinhamento ao centro com 90 colunas
    """
    return f'{title:^90}', f'{n:^90}'


@description
def example7() -> Container | Generator:
    """Uso de valores com formatação no alinhamento para strings.

    f'{title:>90}' alinhamento a esquerda com 90 colunas
    """
    return f'{title:>90}', f'{pi:>90}'


@description
def example8() -> Container | Generator:
    """Uso de valores com formatação numérica.
    f'{n:,}' milhar.
    """
    return f'{n:,}', f'{number:,}', f'{pi:,}', 100


@description
def example9() -> Container | Generator:
    """Uso de valores com formatação numérica.
    f'{n:.0f}' decimal, onde 0 é o numero de casas.
    """
    return f'{n:.1f}', f'{number:.2f}', f'{pi:.3f}', f'{100:.4f}'


@description
def example10() -> Container | Generator:
    """Uso de valores com formatação numérica com decimal e milhar.
    f'{n:,.0f}' decimal, onde 0 é o numero de casas.
    """
    return f'{n:,.1f}', f'{number:,.2f}', f'{pi:,.3f}', f'{100:,.4f}'


@description
def example11() -> Container | Generator:
    """Uso de valores com formatação percentual.
    f'{n:.0%}' decimal, onde 0 é o numero de casas.
    """
    return f'{n:.1%}', f'{number:.2%}', f'{pi:.3%}', f'{100:.4%}'


@description
def example12() -> Container | Generator:
    """Uso de valores com formatação percentual e milhar.
    f'{n:.0%}' decimal, onde 0 é o numero de casas.
    """
    return f'{n:,.1%}', f'{number:,.2%}', f'{pi:,.3%}', f'{100:,.4%}'


@description
def example13() -> Container | Generator:
    """Formatar base para Octal.
    f'{100:0o}'.
    """
    return f'{100:0o}', f'{n:0o}'


@description
def example14() -> Container | Generator:
    """Formatar base para binario.
    f'{100:0b}'.
    """
    return f'{100:0b}', f'{n:0b}'


@description
def example15() -> Container | Generator:
    """Formatar base para binario.
    f'{100:0x}'.
    """
    return (
        f'{100:0x}',
        f'{n:0X}',
        f'{number:0x}',
    )


@description
def example16() -> Container | Generator:
    """Formatar datas."""
    hoje = datetime.now()
    return (
        f'{hoje:%F}',
        f'{hoje:%c}',
        f'{hoje:%FT%T.%f}',
    )


@description
def example17() -> Container | Generator:
    """Formatar com notação cientifica.
    f'{100:.3e}' == 1.000e+02.
    """
    datetime.now()
    return f'{pi:e}', f'{n:.1e}', f'{n:.2e}', f'{number:.3e}', f'{100:.4e}'


@description
def example18() -> Container | Generator:
    """Exibir __repr__ ou __str__."""
    u = User('Ana Brito', datetime.now())
    return (
        f'{u!s}',
        f'{u!r}',
    )


@description
def example19() -> Container | Generator:
    """Exibir __repr__ ou __str__."""
    u = User('Ada Brito', datetime.now())
    return f'{u}', f'{type(u.born)}', f'{u.born!s}', f'{u.born!r}'


@description
def example20() -> Container | Generator:
    """Exibir __repr__ ou __str__."""
    u = User('Ada Brito', datetime.now())
    return f'{u!s}', f'{u!r}', f'{u!a}'


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
        example10,
        example11,
        example12,
        example13,
        example14,
        example15,
        example16,
        example17,
        example18,
        example19,
        example20,
    ]
    successive_execution(funcs)


if __name__ == '__main__':  # pragma: no cover
    run()
