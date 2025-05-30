"""Module."""

from typing import NoReturn

import flet as ft

__author__ = '@britodfbr'  # pragma: no cover

import httpx


def get_content(url: str = '') -> str:
    """Get content from API."""
    url = url or 'https://loripsum.net/api/10/long/headers/links/dl/ol/bq/code'
    resp = httpx.get(url)
    return resp.text


conteudo = get_content()


class MyView(ft.UserControl):
    """View personalizado."""

    def __init__(self, *args, **kwargs):
        """Myview init."""
        super().__init__(*args, **kwargs)

    def build(self):
        """Build Myview."""
        return ft.Container(
            content=ft.Column(
                controls=[ft.Text(selectable=True, value=conteudo)],
            ),
        )


def main(page: ft.Page) -> NoReturn:
    """Run it."""
    page.scroll = 'auto'
    page.add(MyView())


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main)
