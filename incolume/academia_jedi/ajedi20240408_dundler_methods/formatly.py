"""Module."""

from __future__ import annotations

import datetime as dt

import pytz
from config import settings

__author__ = '@britodfbr'  # pragma: no cover

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


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
        self.spec = {
            'kg': f'{self.grams / 1000:.2f}Kg',
            'desc': f'{self.grams / 1000:.2f}Kg ({self.grams}g) de {self.name} em {self.date.isoformat()}',
        }

    def __eq__(self, other: Self) -> bool:
        """Check if fruit equals."""
        return self.__dict__ == other.__dict__

    def __format__(self, format_spec: str) -> str:
        """Define format show."""
        return self.spec.get(format_spec)
