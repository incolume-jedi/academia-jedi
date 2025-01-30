"""Module."""

from enum import Enum, auto
from typing import NamedTuple

from icecream import ic

__author__ = '@britodfbr'  # pragma: no cover


class TelefoneReference(Enum):
    """Class TelefoneReference."""

    RESIDENCIAL = auto()
    COMERCIAL = auto()
    RECADO = auto()

    def __repr__(self):
        """Repr."""
        return self.name


class TelefoneTipo(Enum):
    """TelefoneTipo class."""

    FIXO: int = auto()
    MOVEL: int = auto()

    def __repr__(self):
        """Repr."""
        return self.name


class Telefone(NamedTuple):
    """Telefone class."""

    ddd: str
    numero: str
    tipo: TelefoneTipo
    referencia: TelefoneReference = None


class Pessoa(NamedTuple):
    """Pessoa representation."""

    nome: str
    sobrenome: str
    telefones: list[Telefone]


def run():
    """Run it."""
    ic(TelefoneTipo.MOVEL.__dict__, list(TelefoneTipo))
    pessoa = Pessoa(
        'Bob',
        'Smith',
        [
            Telefone(
                '61',
                '99999-0000',
                TelefoneTipo.MOVEL,
                TelefoneReference.RESIDENCIAL,
            ),
        ],
    )
    ic(pessoa)


if __name__ == '__main__':  # pragma: no cover
    run()
