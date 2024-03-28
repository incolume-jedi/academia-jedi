"""Exemplo de componentes com bordas angulares."""

__author__ = '@britodfbr'  # pragma: no cover

from typing import NoReturn

import flet as ft


def main(page: ft.Page) -> NoReturn:
    """Run it."""
    t = ft.Row(
        height=40,
        vertical_alignment=ft.CrossAxisAlignment.STRETCH,
        controls=[
            ft.TextField(
                label='E-mail',
                border_radius=ft.border_radius.all(0),
            ),
            ft.FilledButton(
                text='Enviar',
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=0),
                ),
            ),
        ],
    )

    page.add(t)


ft.app(target=main)
