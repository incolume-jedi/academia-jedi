__author__ = "@britodfbr"  # pragma: no cover

from dataclasses import dataclass


class Currency:
    def __init__(self,
                 value: float = .0, *, sigla: str = 'BRL', symbol: str = 'R$'):
        self.sigla = sigla
        self.symbol = symbol
        self.value = value

    def __str__(self):
        return 'Currency({sigla} {value:0.2f})'.format(**self.__dict__)

    def __repr__(self):
        return '{symbol} {value:0.2f}'.format(**self.__dict__)

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __add__(self, other):
        if isinstance(other, Currency) and (self.sigla == other.sigla):
            self.value += other.value
        else:
            self.value += other
        return self

    def __iadd__(self, other):
        return self.__add__(other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Currency) and (self.sigla == other.sigla):
            self.value -= other.value
        else:
            self.value -= other
        return self

    def __isub__(self, other):
        return self.__sub__(other)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        self.value *= other
        return self

    def __imul__(self, other):
        return self.__mul__(other)

    def __rmul__(self, other):
        return self.__mul__(other)


@dataclass
class NC:
    value: float = .0
    sigla: str = 'BRL'
    symbol: str = 'R$'

    def __str__(self):
        return 'Currency({sigla} {value:0.2f})'.format(**self.__dict__)

    def __repr__(self):
        return '{symbol} {value:0.2f}'.format(**self.__dict__)

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value
