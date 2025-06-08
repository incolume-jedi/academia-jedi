"""Example for flet WebView."""

from typing import NoReturn

import flet as ft
from icecream import ic


def main(page: ft.Page) -> NoReturn:
    """Run it."""
    wv = ft.WebView(
        'https://flet.dev',
        expand=True,
        on_page_started=lambda _: ic('Page started'),
        on_page_ended=lambda _: ic('Page ended'),
        on_web_resource_error=lambda e: ic('Page error:', e.data),
    )
    page.add(wv)


if __name__ == '__main__':
    ft.app(main)
