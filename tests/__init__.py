"""Tests module."""

from config import settings
from icecream import ic

__author__ = '@britodfbr'  # pragma: no cover

ic.disable()
if settings.debug_mode:
    ic.enable()
