"""Jokenpo module."""
from enum import Enum
from dataclasses import dataclass

__author__ = "@britodfbr"  # pragma: no cover


class Jokenpo(Enum):
    """"""
    PAPEL = 1
    TESOURA = 2
    PEDRA = 3


@dataclass
class Jogador:
    nome: str
    lance: Jokenpo
    vitorias: int = 0
    derrotas: int = 0
    empates: int = 0

    def __lt__(self, __value: 'Jogador') -> bool:
        """Menor que."""
        if __value.lance.value > self.lance.value:
            print(
                f'{__value.lance.name} x {self.lance.name}: {self.nome} lose')
            __value.vitorias += 1
            self.derrotas += 1
            return True
        return False

    def __ilt__(self, __value: 'Jogador') -> bool:
        return self.__lt__(__value)

    def __eq__(self, __value: 'Jogador') -> bool:
        """Equal."""
        if __value.lance.value == self.lance.value:
            print(
                f'{__value.lance.name} x {self.lance.name}: {__value.nome} empate')
            self.empates += 1
            __value.empates += 1
            return True
        return False

    def __gt__(self, __value: 'Jogador') -> bool:
        """Maior que."""
        if __value.lance.value < self.lance.value:
            print(
                f'{__value.lance.name} x {self.lance.name}: {self.nome} wins')
            __value.derrotas += 1
            self.vitorias += 1
            return True
        return False

    def __igt__(self, __value: 'Jogador') -> bool:
        """Maior que."""
        return self.__gt__(__value)
