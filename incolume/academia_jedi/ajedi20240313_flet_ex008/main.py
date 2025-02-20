"""Módulo protótipo."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

import logging
from pathlib import Path

import flet as ft
from config import settings
from controllers.components import (
    first_name,
    greetings,
    last_name,
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
