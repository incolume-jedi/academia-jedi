"""Scrap imdb."""

import logging

from config import settings

__author__ = '@britodfbr'  # pragma: no cover

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.DEBUG,
    format=settings.format_log,
    datefmt=settings.datefmt,
)
