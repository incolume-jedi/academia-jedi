"""Components modules."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

import logging
from pathlib import Path

import flet as ft
from config import settings

__author__ = '@britodfbr'  # pragma: no cover

first_name = ft.Ref[ft.TextField]()
last_name = ft.Ref[ft.TextField]()
greetings = ft.Ref[ft.Column]()


def popup_menu_item(**kwargs: str) -> ft.PopupMenuItem:
    """PopMenuItem for project."""
    text = kwargs.get('text', '')
    on_click = kwargs.get('on_click') or (
        lambda _: logging.debug(text.casefold())
    )
    kwargs.update({'on_click': on_click})
    return ft.PopupMenuItem(**kwargs)


class SetAppBar(ft.AppBar):
    """Class SetAppBar."""

    # Componente defeituoso

    def __init__(
        self,
        page: ft.Page,
        logo: str = '',
        title: str = '',
        *args: str,
        **kwargs: str,
    ):
        """Init it."""
        super().__init__(*args, **kwargs)
        self.page = page
        self.logo = (
            logo or Path('images', 'icons', 'icon-nobg-1024.png').as_posix()
        )
        self.title = title or 'Planalto Legis'
        self.bg_color = settings.blue
        self.color = ft.colors.WHITE

    def build(self) -> ft.AppBar:
        """Define AppBar."""
        return ft.AppBar(
            bgcolor=self.bg_color,
            color=self.color,
            leading=ft.Image(
                src=self.logo,
            ),
            leading_width=40,
            toolbar_height=self.page.window_height * 0.1,
            title=ft.Text(self.title, weight=ft.FontWeight.W_500),
            center_title=True,
            actions=[
                ft.PopupMenuButton(
                    visible=True,
                    icon=ft.icons.MENU,
                    items=[
                        ft.PopupMenuItem(),
                        ft.Divider(),
                        ft.PopupMenuItem(
                            text='Busca Avançada',
                            on_click=lambda _: logging.debug('busca avançada'),
                        ),
                        ft.PopupMenuItem(
                            text='Constituição',
                            on_click=lambda _: logging.debug('constituição'),
                        ),
                        ft.PopupMenuItem(
                            text='Códigos',
                            on_click=lambda _: logging.debug('códigos'),
                        ),
                        ft.PopupMenuItem(
                            text='Estatutos',
                            on_click=lambda _: logging.debug('estatutos'),
                        ),
                        ft.PopupMenuItem(
                            text='Favoritos',
                            on_click=lambda _: logging.debug('favoritos'),
                        ),
                        ft.PopupMenuItem(
                            text='Resenha',
                            on_click=lambda _: logging.debug('resenha'),
                        ),
                        ft.PopupMenuItem(
                            text='Ajuda',
                            on_click=lambda _: logging.debug('ajuda'),
                        ),
                    ],
                ),
            ],
        )
