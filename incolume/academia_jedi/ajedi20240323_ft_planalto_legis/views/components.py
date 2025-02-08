"""Components."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

import logging
from pathlib import Path
from typing import Any

import flet as ft

__author__ = '@britodfbr'  # pragma: no cover

from incolume.academia_jedi.ajedi20240323_ft_planalto_legis.views.template import (
    BLUE,
    IMAGES,
)


def set_navbar(page: ft.Page) -> ft.NavigationBar:
    """Define Navigation Bar."""
    page.update()
    return ft.NavigationBar(
        visible=True,
        bgcolor=BLUE,
        surface_tint_color=ft.colors.WHITE,
        shadow_color=ft.colors.BLACK87,
        indicator_color=ft.colors.BLUE,
        selected_index=1,
        destinations=[
            ft.NavigationDestination(
                icon=ft.icons.CALENDAR_MONTH_ROUNDED,
                tooltip='Resenha diária',
                label='RESENHA',
            ),
            ft.NavigationDestination(
                icon=ft.icons.SEARCH,
                tooltip='Busca avançada',
                label='BUSCA',
            ),
            ft.NavigationDestination(
                icon=ft.icons.STAR_PURPLE500_OUTLINED,
                tooltip='Atos Favoritos',
                label='FAVORITOS',
            ),
            ft.NavigationDestination(
                icon=ft.icons.HELP,
                tooltip='Ajuda',
                label='AJUDA',
            ),
        ],
    )


def set_appbar(page: ft.Page, logo: str = '', title: str = '') -> ft.AppBar:
    """Define AppBar."""
    logo = logo or Path('images', 'icons', 'icon-nobg-1024.png').as_posix()
    title = title.title() or 'Planalto Legis'
    return ft.AppBar(
        bgcolor=BLUE,
        color=ft.colors.WHITE,
        leading=ft.Image(
            src=logo,
        ),
        leading_width=50,
        toolbar_height=page.window_height * 0.1,
        title=ft.Text(title, weight=ft.FontWeight.W_500),
        center_title=True,
        actions=[
            ft.PopupMenuButton(
                visible=True,
                icon=ft.icons.MENU,
                items=[
                    ft.PopupMenuItem(
                        text='Busca Avançada',
                        on_click=lambda _: page.go('/busca'),
                    ),
                    ft.PopupMenuItem(
                        text='Constituição',
                        on_click=lambda _: page.go('/constituicao'),
                    ),
                    ft.PopupMenuItem(
                        text='Códigos',
                        on_click=lambda _: page.go('/codigos'),
                    ),
                    ft.PopupMenuItem(
                        text='Estatutos',
                        on_click=lambda _: page.go('/estatutos'),
                    ),
                    ft.PopupMenuItem(
                        text='Favoritos',
                        on_click=lambda _: page.go('/favoritos'),
                    ),
                    ft.PopupMenuItem(
                        text='Resenha',
                        on_click=lambda _: page.go('/resenha'),
                    ),
                    ft.PopupMenuItem(
                        text='Ajuda',
                        on_click=lambda _: page.go('/ajuda'),
                    ),
                ],
            ),
        ],
    )


def set_bg(page: ft.Page) -> ft.Stack:
    """Define background."""
    return ft.Stack(
        scale=1,
        aspect_ratio=9 / 16,
        width=page.window_width,
        # height=page.window_height - page.appbar.toolbar_height,
        controls=[
            ft.Image(
                src=IMAGES[1].as_posix(),
                aspect_ratio=9 / 16,
                width=page.window_width,
                height=page.window_height,
                fit=ft.ImageFit.COVER,
                opacity=1,
            ),
        ],
    )


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
