"""Page views."""

import flet as ft
from templates import MyAppBar

__author__ = '@britodfbr'  # pragma: no cover


def home(page: ft.Page):
    """Home page."""
    return (
        ft.View(
            route='/',
            controls=[
                MyAppBar(page).build(),
                ft.Text('Homepage'),
            ],
        ),
    )
