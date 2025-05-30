"""Module."""

from __future__ import annotations

import datetime as dt
import sys
from copy import copy
from dataclasses import dataclass, field
from typing import NoReturn

__author__ = '@britodfbr'  # pragma: no cover

# ruff: noqa: F811, F821

if sys.version_info < (3, 10):  # noqa: UP036
    sys.exit('This run only Python 3.10 or higher')


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
    def date(self) -> None:
        """Get date."""
        return self.__date.isoformat()

    @date.setter
    def date(self, value: dt.datetime) -> NoReturn:
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

    def __repr__(self) -> str:
        """Dundler repr."""
        o = copy(self)
        return f'{o:desc}'


@dataclass
class Basket:
    """Basket class."""

    content: list[Fruit3]

    def __getitem__(self, item):
        """Getitem."""
        return [
            fruit for fruit in self.content if fruit.name.casefold() == item
        ]


if __name__ == '__main__':
    ic(sys.modules)
