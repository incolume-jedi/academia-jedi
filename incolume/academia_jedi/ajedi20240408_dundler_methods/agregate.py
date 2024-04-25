"""Module."""
from copy import copy
from dataclasses import dataclass, field
import datetime as dt

__author__ = '@britodfbr'  # pragma: no cover


@dataclass(kw_only=True)
class Fruit3:
    """Class Fruit3."""

    name: str
    grams: float = field(default=0)
    date: dt.datetime = field(default_factory=dt.datetime.now)

    def __post_init__(self):
        """Post init."""
        self.__date: self.date

    @property
    def date(self):
        """Get date."""
        return self.__date.isoformat()

    @date.setter
    def date(self, value: dt.datetime):
        """Set date."""
        self.__date = value

    def __format__(self, format_spec: str) -> str:
        """Define format show."""
        match format_spec:
            case 'kg':
                return f'{self.grams / 1000:.2f}Kg'
            case 'desc':
                return (
                    f'{self.grams / 1000:.2f}Kg ({self.grams}g) de'
                    f' {self.name} em {self.date}'
                )

    def __repr__(self):
        """Dundler repr."""
        o = copy(self)
        return f'{o:desc}'


@dataclass
class Basket:
    content: list[Fruit3]

    def __getitem__(self, item):
        """Getitem."""
        return [
            fruit for fruit in self.content if fruit.name.casefold() == item
        ]
