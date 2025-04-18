"""Tests module."""
from icecream import ic
from config import settings

__author__ = '@britodfbr'  # pragma: no cover

ic.disable()
if settings.debug_mode:
    ic.enable()
