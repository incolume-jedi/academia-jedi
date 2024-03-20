"""Módulo protótipo."""

from pathlib import Path

import flet as ft
import logging
from config import settings
from controllers.components import (
    first_name,
    last_name,
    greetings,
    popup_menu_item,
)


def main(page: ft.Page) -> None:
    """Main function."""
    page.theme_mode = settings.template
    page.window_min_width = 320
    # Appbar
    appbar = ft.AppBar(
        bgcolor=settings.blue,
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
                    popup_menu_item(
                        icon=ft.icons.MILITARY_TECH,
                        text='test',
                        on_click=lambda _: logging.debug('ok'),
                    ),
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
    page.appbar = appbar

    def btn_click(e):
        logging.debug('%s', type(e))
        if not first_name.current.value:
            first_name.current.error_text = 'Please enter with first_name'
            page.update()
            return

        first_name.current.error_text = ''

        if not last_name.current.value:
            last_name.current.error_text = 'Please enter with last_name'
            page.update()
            return

        last_name.current.error_text = ''

        greetings.current.controls.append(
            ft.Text(
                f'Hello, {first_name.current.value}'
                f' {last_name.current.value}!',
            ),
        )
        first_name.current.value = ''
        last_name.current.value = ''
        page.update()
        first_name.current.focus()

    page.add(
        ft.TextField(
            ref=first_name,
            label='First name',
            autofocus=True,
        ),
        ft.TextField(ref=last_name, label='Last name'),
        ft.ElevatedButton('Say hello!', on_click=btn_click),
        ft.Column(ref=greetings),
    )


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main)
