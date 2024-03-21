""""""
from typing import NoReturn

import flet as ft

__author__ = "@britodfbr"  # pragma: no cover


def main(page: ft.Page) -> NoReturn:
    """Run it."""
    page.add(ft.Text(f"Initial route: {page.route}"))

    def route_change(e: ft.RouteChangeEvent):
        """Route change."""
        page.add(ft.Text(f"New route: {e.route}"))

    def route_compras(e: ft.ControlEvent):
        """Route compras."""
        page.route = '/compras'
        page.update()

    page.on_route_change = route_change
    page.update()
    page.add(ft.ElevatedButton('/compras', on_click=route_compras))


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
