"""Templates."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

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
        bgcolor: str = '',
        *args: Any,
        **kwargs: Any,
    ):
        """Init it."""
        super().__init__(*args, **kwargs)
        self.page = page
        self.title = title or 'Home'
        self.bgcolor = bgcolor or ft.colors.SURFACE_VARIANT

    def build(self):
        """Build it."""
        return ft.AppBar(
            title=ft.Text(self.title),
            bgcolor=self.bgcolor,
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
