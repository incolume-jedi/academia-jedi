"""Jokenpo module."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from secrets import choice
from typing import Self

__author__ = '@britodfbr'  # pragma: no cover

# ruff: noqa: T201


class Jokenpo(Enum):
    """Jokenpo enumerate."""

    PAPEL = 1
    TESOURA = 2
    PEDRA = 3

    @classmethod
    def _missing_(cls, value: str | int) -> Self:
        """Missing values.

        Args:
            value (int or str): Jokenpo value

        Returns:
            Jokenpo: self
        """
        if isinstance(value, str):
            value = value.upper()
            if value.isdigit():
                value = int(value)

        for member in cls:
            if value in (member.value, member.name):
                return member
        return None

    def __eq__(self, other: Self) -> Self:
        """Equity.

        Args:
            other (_type_): _description_

        Returns:
            _type_: _description_
        """
        return super().__eq__(other)

    def __lt__(self, other: Self) -> bool:
        """Less than.

        Args:
            other (Self): _description_

        Returns:
            bool: _description_
        """
        result = self.value < other.value
        if (
            self.value == self.PAPEL.value and other.value == self.PEDRA.value
        ) or (
            self.value == self.PEDRA.value and other.value == self.PAPEL.value
        ):
            return not result
        return result

    def __ilt__(self, other: Self) -> bool:
        """Less than.

        Args:
            other (Self): _description_

        Returns:
            bool: _description_
        """
        return self.__lt__(other)

    def __gt__(self, other: Self) -> bool:
        """Greater than.

        Args:
            other (Self): _description_

        Returns:
            bool: _description_
        """
        result = self.value > other.value
        if (
            self.value == self.PEDRA.value and other.value == self.PAPEL.value
        ) or (
            self.value == self.PAPEL.value and other.value == self.PEDRA.value
        ):
            return not result
        return result


@dataclass
class Jogador:
    """Jogador dataclass.

    Returns:
        _type_: _description_
    """

    nome: str
    lance: Jokenpo = field(repr=False)
    vitorias: int = 0
    derrotas: int = 0
    empates: int = 0


def start_jokenpo(jogador1: Jogador, jogador2: Jogador) -> str:
    """Inicia jogo de jokenpo.

    Inicia a rodada e contabiliza os resultados para cada jogador;

    Args:
        jogador1 (Jogador): jogador da rodada
        jogador2 (Jogador): jogador da rodada

    Returns:
        str: resultado da rodada
    """
    result = ''
    if jogador1.lance > jogador2.lance:
        jogador1.vitorias += 1
        jogador2.derrotas += 1
        result = (
            f'{jogador1.nome} X {jogador2.nome}: {jogador1.nome} Ganhou!!!'
        )
    if jogador1.lance < jogador2.lance:
        jogador1.derrotas += 1
        jogador2.vitorias += 1
        result = (
            f'{jogador1.nome} X {jogador2.nome}: {jogador2.nome} Ganhou!!!'
        )
    if jogador1.lance == jogador2.lance:
        jogador1.empates += 1
        jogador2.empates += 1
        result = f'{jogador1.nome} X {jogador2.nome}: Empate.'

    return result


def jogo():  # pragma: no cover
    """Run game."""
    name = 'Jogo JOKENPO'
    line = '-=-' * 10
    sair = ['0', 'q', 'quit', 'sair', 's']
    title = f'{line}\n{name}\n{line}\n'
    menu = f""" {title}Opções disponíveis:
    1 - papel
    2 - tesoura
    3 - pedra
    0 - sair
{line}\n
    """
    print(f'{title}\n\nIniciado o {name}. Contra o computador.')
    nome = input('    Qual o teu nome? ')
    members = Jokenpo.__members__
    print(menu)
    jogador = Jogador(nome, lance=None)
    computador = Jogador('PC', lance=None)
    while (op := input('    Escolha uma opção: ')) not in members:
        print(op)
        if op not in [str(x) for x in members] + sair:
            print('\n\nInforme apenas as opções do Menu.\n\n\n')
        if op in sair:
            break
        jogador.lance = Jokenpo(op)
        computador.lance = Jokenpo(choice(range(1, 4)))
        print(
            'JO \nKEN \nPO\n'
            f'{line}\n{jogador.nome}({jogador.lance.name})\n'
            f'{computador.nome}({computador.lance.name})\n'
            f'{line}\n',
        )
        print(start_jokenpo(jogador, computador))

        print(menu)
    print(jogador)
    print(computador)


if __name__ == '__main__':
    jogo()
