"""Components modules."""

import flet as ft
import logging
from pathlib import Path
from config import settings

__author__ = '@britodfbr'  # pragma: no cover

first_name = ft.Ref[ft.TextField]()
last_name = ft.Ref[ft.TextField]()
greetings = ft.Ref[ft.Column]()


def popup_menu_item(**kwargs) -> ft.PopupMenuItem:
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
