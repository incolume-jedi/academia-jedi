"""Example"""

import logging

import flet as ft
from template import BLUE, IMAGES
from pathlib import Path


def main0(page: ft.Page) -> None:
    """Main estructure."""
    page.window_always_on_top = True
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.title = 'Planalto Legis'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_min_width = 450
    page.window_min_height = 720
    page.padding = 0
    page.window_width = page.window_min_width
    page.window_height = page.window_min_height
    page.scroll = ft.ScrollMode.AUTO
    page.window_bgcolor = ft.colors.BLACK

    # Background
    background = ft.Stack(
        expand=True,
        width=page.window_width,
        height=page.window_height,
        controls=[
            ft.Image(
                src=IMAGES[0].as_posix(),
                width=page.window_width,
                height=page.window_height,
                fit=ft.ImageFit.COVER,
                opacity=1,
            ),
            ft.Row(
                [
                    ft.Text(
                        'Image title',
                        color='yellow',
                        size=40,
                        weight='bold',
                        opacity=0.5,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
    )

    # Appbar
    appbar = ft.AppBar(
        bgcolor=BLUE,
        color=ft.colors.WHITE,
        leading=ft.Image(
            src=Path('images', 'icons', 'icon-nobg-1024.png').as_posix(),
        ),
        leading_width=40,
        title=ft.Text('Planalto Legis', weight=ft.FontWeight.W_500),
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

    # Navbar
    navbar = ft.NavigationBar(
        visible=True,
        bgcolor=BLUE,
        surface_tint_color=ft.colors.WHITE,
        shadow_color=ft.colors.PURPLE_100,
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
                label='AJUDA',
            ),
        ],
    )

    page.appbar = appbar
    page.navigation_bar = navbar
    page.add(background)


if __name__ == '__main__':
    ft.app(target=main0)
