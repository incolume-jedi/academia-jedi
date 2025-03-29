"""Estudo sobre metodos mágicos."""

__author__ = '@britodfbr'  # pragma: no cover


from dataclasses import dataclass


class Currency:
    """Currency class."""

    def __init__(
        self,
        value: float = 0.0,
        *,
        sigla: str = 'BRL',
        symbol: str = 'R$',
    ) -> None:
        """Init class."""
        self.sigla = sigla
        self.symbol = symbol
        self.value = value

    def __str__(self) -> str:
        """Str class."""
        return 'Currency({sigla} {value:0.2f})'.format(**self.__dict__)

    def __repr__(self) -> str:
        """Repr class."""
        return '{symbol} {value:0.2f}'.format(**self.__dict__)

    def __lt__(self, other):
        """Less than."""
        return self.value < other.value

    def __gt__(self, other):
        """Grand than."""
        return self.value > other.value

    def __add__(self, other):
        """Add."""
        if isinstance(other, Currency) and (self.sigla == other.sigla):
            self.value += other.value
        else:
            self.value += other
        return self

    def __iadd__(self, other):
        """Inverse add."""
        return self.__add__(other)

    def __radd__(self, other):
        """Reverse add."""
        return self.__add__(other)

    def __sub__(self, other):
        """Sub."""
        if isinstance(other, Currency) and (self.sigla == other.sigla):
            self.value -= other.value
        else:
            self.value -= other
        return self

    def __isub__(self, other):
        """Inverse sub."""
        return self.__sub__(other)

    def __rsub__(self, other):
        """Reverse sub."""
        return self.__sub__(other)

    def __mul__(self, other):
        """Mult."""
        self.value *= other
        return self

    def __imul__(self, other):
        """Inverse mult."""
        return self.__mul__(other)

    def __rmul__(self, other):
        """Reverse mult."""
        return self.__mul__(other)

    def __floordiv__(self, other):
        """Floordiv."""
        if isinstance(other, Currency) and self.sigla == other.sigla:
            self.value //= other.value
        else:
            self.value //= other
        return self

    def __rfloordiv__(self, other):
        """Reverse floordiv."""
        return self.__floordiv__(other)

    def __truediv__(self, other):
        """True div."""
        if isinstance(other, Currency) and self.sigla == other.sigla:
            self.value /= other.value
        else:
            self.value /= other
        return self

    def __rtruediv__(self, other):
        """True div reverse."""
        return self.__truediv__(other)

    def __neg__(self):
        """Negativ."""
        self.value *= -1
        return self


@dataclass
class NC:
    """NC class."""

    value: float = 0.0
    sigla: str = 'BRL'
    symbol: str = 'R$'

    def __str__(self) -> str:
        """Str class."""
        return 'Currency({sigla} {value:0.2f})'.format(**self.__dict__)

    def __repr__(self) -> str:
        """Repr class."""
        return '{symbol} {value:0.2f}'.format(**self.__dict__)

    def __lt__(self, other):
        """Less than."""
        return self.value < other.value

    def __gt__(self, other):
        """Grand than."""
        return self.value > other.value
