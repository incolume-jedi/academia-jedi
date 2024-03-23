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
            MyAppBar(page, title='Constituição').build(),
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
