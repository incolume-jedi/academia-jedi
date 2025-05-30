"""Roteamento entre páginas."""

import logging
from typing import NoReturn

import flet as ft
from router import route_change

__author__ = '@britodfbr'  # pragma: no cover


def main(page: ft.Page) -> NoReturn:
    """Run it."""
    page.title = 'sistemas de roteamento'
    page.add(ft.Text(f'Initial route: {page.route}'))

    def view_pop(e: ft.ControlEvent) -> NoReturn:
        """View pop."""
        logging.debug(e)
        e.page.views.pop()
        e.page.go(page.views[-1])

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main, view=ft.AppView.FLET_APP_WEB)
