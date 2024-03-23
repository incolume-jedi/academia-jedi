"""Templates."""

import logging
from typing import Any

import flet as ft

__author__ = '@britodfbr'  # pragma: no cover


class MyAppBar(ft.UserControl):
    """Appbar personalizado."""

    def __init__(
        self,
        page: ft.Page,
        title: str = '',
        *args: Any,
        **kwargs: Any,
    ):
        """Init it."""
        super().__init__(*args, **kwargs)
        self.page = page
        self.title = title or 'Home'

    def build(self):
        """Build it."""
        return ft.AppBar(
            title=ft.Text(self.title),
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(
                            text='Home',
                            on_click=lambda _: self.page.go('/'),
                        ),
                        ft.PopupMenuItem(
                            text='Busca Avançada',
                            on_click=lambda _: self.page.go('/busca-avancada'),
                        ),
                        ft.PopupMenuItem(
                            text='Constituição',
                            on_click=lambda _: self.page.go('/constituicao'),
                        ),
                        ft.PopupMenuItem(
                            text='Códigos',
                            on_click=lambda _: self.page.go('/codigos'),
                        ),
                        ft.PopupMenuItem(
                            text='Estatutos',
                            on_click=lambda _: self.page.go('/estatutos'),
                        ),
                        ft.PopupMenuItem(
                            text='Favoritos',
                            on_click=lambda _: self.page.go('/favoritos'),
                        ),
                        ft.PopupMenuItem(
                            text='Resenha',
                            on_click=lambda _: self.page.go('/resenha'),
                        ),
                        ft.PopupMenuItem(
                            text='Ajuda',
                            on_click=lambda _: self.page.go('/ajuda'),
                        ),
                        ft.PopupMenuItem(
                            text='Settings',
                            on_click=lambda _: self.page.go('/settings'),
                        ),
                        ft.PopupMenuItem(
                            text='Fechar',
                            icon=ft.icons.CLOSE_ROUNDED,
                            on_click=lambda _: self.page.go('/exit'),
                        ),
                    ],
                ),
            ],
        )

    def __call__(self, *args: Any, **kwargs: Any) -> ft.AppBar:
        """Call it."""
        logging.debug('args: %s', args)
        logging.debug('kwargs: %s', kwargs)
        return self.build()
