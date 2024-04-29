"""Module."""

__author__ = '@britodfbr'  # pragma: no cover

from pathlib import Path
from typing import NoReturn

import flet as ft

md1 = Path(__file__).parent.joinpath('example.md')


def main(page: ft.Page) -> NoReturn:
    """Run it."""
    page.scroll = 'auto'
    page.add(
        ft.Markdown(
            md1.read_text(),
            selectable=True,
            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
            on_tap_link=lambda e: page.launch_url(e.data),
        ),
    )


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main)
