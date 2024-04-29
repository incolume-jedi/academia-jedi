"""Module."""

from pathlib import Path
from typing import NoReturn

import flet as ft
import httpx

__author__ = '@britodfbr'  # pragma: no cover


def get_content(url_api: str = '') -> dict:
    """Get content from API."""
    url_api = url_api or 'https://httpbin.org/anything'
    result = httpx.post(
        url_api,
        data=Path(__file__).parent.joinpath('content.md').read_text(),
    )
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
                        value=conteudo.get('data'),
                        selectable=True,
                        text_align=ft.TextAlign.JUSTIFY,
                    ),
                    ft.Divider(),
                    ft.Markdown(
                        value=conteudo.get('data'),
                        selectable=True,
                        extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
                        on_tap_link=lambda e: e.page.launch_url(e.data),
                    ),
                    ft.Divider(),
                    ft.Markdown(
                        value=httpx.get(
                            url='https://loripsum.net/api/10/long/'
                            'headers/links/dl/ol/bq/code',
                        ).text,
                        selectable=True,
                        extension_set=ft.MarkdownExtensionSet.COMMON_MARK,
                        on_tap_link=lambda e: e.page.launch_url(e.data),
                    ),
                ],
            ),
        )


def main(page: ft.Page) -> NoReturn:
    """Run it."""
    page.scroll = 'auto'
    page.add(MyView())


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main)
