"""Page views."""

import flet as ft
from templates import MyAppBar

__author__ = '@britodfbr'  # pragma: no cover


def home(page: ft.Page) -> ft.View:
    """Home page."""
    return ft.View(
        route='/',
        controls=[
            MyAppBar(page).build(),
            ft.Text('Homepage'.upper()),
        ],
    )


def not_found(page: ft.Page) -> ft.Control:
    """404 page."""
    return ft.View(
        route='/404',
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            MyAppBar(page, title='Not Found').build(),
            ft.Text(
                'Recurso não encontrado!',
                color='red',
                weight='bold',
                text_align=ft.TextAlign.CENTER,
                size=40,
            ),
        ],
    )
