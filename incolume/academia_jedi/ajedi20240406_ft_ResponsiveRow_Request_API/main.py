"""Module.


baseado em https://www.youtube.com/watch?v=EUEUO8Vfomc
"""

import logging
from typing import NoReturn

import flet as ft
import httpx
from config import settings

__author__ = '@britodfbr'  # pragma: no cover
# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

logging.basicConfig(level=logging.INFO, format=settings.format_log)


class Home(ft.UserControl):
    """Class home."""

    def __init__(self, count: int = 0, *args: str, **kwargs: str):
        """Init Home."""
        super().__init__(*args, **kwargs)
        self.count = count
        self.body = ft.ResponsiveRow()
        self.loader = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.ProgressRing(
                    width=90,
                    height=90,
                    visible=True,
                ),
            ],
        )

    @property
    def count(self):
        """Count value."""
        return self._count

    @count.setter
    def count(self, value: int) -> None:
        """Count value."""
        self._count = max(value, 10)

    def did_mount(self):
        """Did mount."""
        url: str = (
            'https://random-data-api.com/'
            f'api/users/random_user?size={self.count}'
        )
        try:
            response = httpx.get(url)
            logging.info(response)

            data = response.json()
            for user in data:
                self.body.controls.append(
                    ft.Column(
                        col={'sm': 6, 'md': 3, 'xl': 3},
                        controls=[
                            ft.Card(
                                elevation=10,
                                content=ft.Container(
                                    bgcolor=ft.colors.BLUE_200,
                                    content=ft.Column([
                                        ft.Image(
                                            src=user.get('avatar'),
                                            width=100,
                                            height=100,
                                        ),
                                        ft.Text(f'UID: {user.get("uid")}'),
                                        ft.Text(
                                            'Username: '
                                            f'{user.get("username")}',
                                        ),
                                        ft.Text(f'Email: {user.get("email")}'),
                                    ]),
                                ),
                            ),
                        ],
                    ),
                )
            self.loader.visible = False

        except AssertionError:
            logging.exception('...')
        self.update()

    def build(self):
        """Build it."""
        return ft.Column([
            self.body,
            self.loader,
        ])


def main(page: ft.Page) -> NoReturn:
    """Run it."""
    page.scroll = 'auto'
    page.padding = 0
    page.title = 'Galeria de Usuários'
    page.add(Home())


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main, port=8000)
