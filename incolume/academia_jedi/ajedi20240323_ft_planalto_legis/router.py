"""Router module."""

__author__ = '@britodfbr'  # pragma: no cover

import logging
from typing import NoReturn
import flet as ft


def view_pop(e: ft.ControlEvent) -> NoReturn:
    """View pop."""
    logging.debug(e)
    e.page.views.pop()
    e.page.go(e.page.views[-1])


def route_change(route: str):
    """"""
