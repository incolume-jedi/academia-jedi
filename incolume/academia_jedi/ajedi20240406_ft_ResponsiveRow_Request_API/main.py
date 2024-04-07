"""Module."""

import logging
from typing import NoReturn
from config import settings
import flet as ft
import httpx

__author__ = '@britodfbr'  # pragma: no cover

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
    def count(self, value: int):
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
                                            f'Username: {user.get("username")}',
                                        ),
                                        ft.Text(f'Email: {user.get("email")}'),
                                    ]),
                                ),
                            )
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
