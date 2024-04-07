"""Module."""

from typing import NoReturn
import json
import flet as ft

__author__ = '@britodfbr'  # pragma: no cover

import httpx


def get_content(url_api: str = '', url_content: str = '') -> dict:
    """Get content from API."""
    url_api = url_api or 'https://httpbin.org/anything'
    url_content = (
        url_content or 'https://loripsum.net/api/10/short/headers/plaintext'
    )
    resp = httpx.get(url_content)
    result = httpx.post(url_api, data=json.dumps(resp.text.split('\n\n')))
    return result.json()


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
                controls=[
                    ft.Text(
                        selectable=True,
                        value=content,
                        text_align=ft.TextAlign.JUSTIFY,
                    )
                    for content in json.loads(conteudo.get('data'))
                ],
            ),
        )


def main(page: ft.Page) -> NoReturn:
    """Run it."""
    page.scroll = 'auto'
    page.add(MyView())


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main)
