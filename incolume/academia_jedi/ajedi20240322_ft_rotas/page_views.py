"""Page views."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

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


def vw_help(page: ft.Page) -> ft.Control:
    """Help page."""
    return ft.View(
        route='/ajuda',
        controls=[
            MyAppBar(page, title='Ajuda').build(),
            ft.Text('Help page...'),
            ft.ElevatedButton(
                text='HOME',
                on_click=lambda _: page.go('/'),
            ),
        ],
    )


def settings(page: ft.Page) -> ft.Control:
    """Settings page."""
    return ft.View(
        route='/settings',
        controls=[
            MyAppBar(page, title='Settings').build(),
            ft.ElevatedButton(
                text='HOME',
                on_click=lambda _: page.go('/'),
            ),
        ],
    )


def busca_avancada(page: ft.Page) -> ft.Control:
    """Busca page."""
    return ft.View(
        route='/busca-avancada',
        controls=[
            MyAppBar(page, title='Busca Avançada').build(),
        ],
    )


def constituicao(page: ft.Page) -> ft.Control:
    """Constituicao page."""
    return ft.View(
        route='/constituicao',
        controls=[
            MyAppBar(page, title='Constituição', bgcolor='red').build(),
        ],
    )


def codigos(page: ft.Page) -> ft.Control:
    """Codigos page."""
    return ft.View(
        route='/codigos',
        controls=[
            MyAppBar(page, title='Códigos').build(),
        ],
    )


def estatutos(page: ft.Page) -> ft.Control:
    """Estatutos page."""
    return ft.View(
        route='/estatutos',
        controls=[
            MyAppBar(page, title='Estatutos').build(),
        ],
    )


def favoritos(page: ft.Page) -> ft.Control:
    """Favoritos page."""
    return ft.View(
        route='/favoritos',
        controls=[
            MyAppBar(page, title='Favoritos').build(),
        ],
    )


def resenha(page: ft.Page) -> ft.Control:
    """Resenha page."""
    return ft.View(
        route='/resenha',
        controls=[
            MyAppBar(page, title='Resenha').build(),
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
                size=30,
            ),
        ],
    )
