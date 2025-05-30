"""Module."""

import datetime as dt
from typing import Optional

import pytz
from config import settings

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


__author__ = '@britodfbr'  # pragma: no cover


class Fruit0:
    """Class fruit0."""

    def __init__(
        self,
        *,
        name: str,
        grams: float,
        date: Optional[dt.datetime] = None,
    ):
        """Init Fruit."""
        self.name = name
        self.grams = grams
        self.date = date or dt.datetime.now(tz=pytz.timezone(settings.tz))

    def __eq__(self, other: Self) -> bool:
        """Check if name equals."""
        return self.name == other.name


class Fruit1:
    """Class fruit1."""

    def __init__(
        self,
        *,
        name: str,
        grams: float,
        date: Optional[dt.datetime] = None,
    ):
        """Init Fruit."""
        self.name = name
        self.grams = grams
        self.date = date or dt.datetime.now(tz=pytz.timezone(settings.tz))

    def __eq__(self, other: Self) -> bool:
        """Check if fruit equals."""
        return self.__dict__ == other.__dict__
