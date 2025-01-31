"""Module."""

from dataclasses import dataclass, field
from enum import Enum, auto
from random import choice

__author__ = '@britodfbr'  # pragma: no cover

# ruff: noqa: S311 T201


class Color(Enum):
    """Color."""

    BLACK: str = '#000000'
    WHITE: str = '#FFFFFF'
    RED: str = '#FF0000'
    GREEN: str = '#00FF00'
    BLUE: str = '#0000FF'

    def __repr__(self):
        """Repr."""
        return f'{self.name}'


class VehicleCategory(Enum):
    """Vehicle category."""

    PASSEIO = auto()
    CARGA = auto()

    def __repr__(self):
        """Repr."""
        return f'{self.name}'


class VehicleType(Enum):
    """Vehicle type."""

    MOTOCICLE = auto()
    VAN = auto()
    HATCH = auto()
    SEDAN = auto()
    WAGON = auto()
    SUV = auto()

    def __repr__(self):
        """Repr."""
        return f'{self.name}'


@dataclass
class Vehicle:
    """Vehicle class."""

    color: Color
    type: VehicleType
    category: VehicleCategory
    wheels: str | int = field(default=0)
    items: list[str] = field(default_factory=list)


@dataclass
class Garagem:
    """Garagem class."""

    _content: list[Vehicle] = field(
        default_factory=list,
        init=False,
        repr=False,
    )

    def __repr__(self):
        """Dundler repr."""
        return f'{self._content}'

    @property
    def content(self):
        """Content getter."""
        return self._content

    @content.setter
    def content(self, value: Vehicle) -> None:
        """Content setter."""
        self._content.append(value)


def run():
    """Run it."""
    vehicles = (
        Vehicle(
            wheels=choice((2, 4)),
            type=choice(list(VehicleType)),
            category=choice(list(VehicleCategory)),
            color=choice(list(Color)),
        )
        for _ in range(10)
    )
    garage = Garagem()
    garage.content = next(vehicles)
    garage.content = next(vehicles)
    garage.content = next(vehicles)
    garage.content = next(vehicles)
    print(garage)


if __name__ == '__main__':  # pragma: no cover
    run()
