"""Module."""

from time import sleep
from typing import NoReturn

import flet as ft

__author__ = '@britodfbr'  # pragma: no cover


def main(page: ft.Page) -> NoReturn:
    """Run it."""
    pr = ft.ProgressRing(width=26, height=26, stroke_width=2)

    page.add(
        ft.Text('Circular progress indicator', style='headlineSmall'),
        ft.Row([pr, ft.Text('Wait for the completion...')]),
        ft.Text('Indeterminate cicrular progress', style='headlineSmall'),
        ft.Column(
            [ft.ProgressRing(), ft.Text("I'm going to run for ages...")],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    for i in range(101):
        pr.value = i * 0.01
        sleep(0.1)
        page.update()


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main)
