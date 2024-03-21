""""""
from typing import NoReturn

import flet as ft

__author__ = "@britodfbr"  # pragma: no cover


def main(page: ft.Page) -> NoReturn:
    """Run it."""
    page.add(ft.Text(f"Initial route: {page.route}"))

    def route_change(e: ft.RouteChangeEvent):
        page.add(ft.Text(f"New route: {e.route}"))

    page.on_route_change = route_change
    page.update()


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
