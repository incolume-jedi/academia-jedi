"""Module."""

__author__ = '@britodfbr'  # pragma: no cover

from typing import Self

import pytz

from config import settings
import datetime as dt


class Fruit2:
    """Class fruit2."""

    def __init__(
        self,
        *,
        name: str,
        grams: float,
        date: dt.datetime | None = None,
    ):
        """Init Fruit."""
        self.name = name
        self.grams = grams
        self.date = date or dt.datetime.now(tz=pytz.timezone(settings.tz))

    def __eq__(self, other: Self) -> bool:
        """Check if fruit equals."""
        return self.__dict__ == other.__dict__

    def __format__(self, format_spec: str) -> str:
        """Define format show."""
        match format_spec:
            case 'kg':
                return f'{self.grams / 1000:.2f}Kg'
            case 'desc':
                return (
                    f'{self.grams / 1000:.2f}Kg ({self.grams}g) de'
                    f' {self.name} em {self.date.isoformat()}'
                )
