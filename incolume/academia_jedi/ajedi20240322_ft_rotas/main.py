"""Roteamento entre páginas."""

import logging
from typing import NoReturn, Any
from templates import MyAppBar
from page_views import home

import flet as ft

__author__ = '@britodfbr'  # pragma: no cover


def main(page: ft.Page) -> NoReturn:
    """Run it."""
    page.title = 'sistemas de roteamento'
    page.add(ft.Text(f'Initial route: {page.route}'))

    def route_change(e: ft.RouteChangeEvent) -> NoReturn:
        """Route change."""
        page.add(ft.Text(f'New route: {e.route}'))
        page.views.clear()
        match page.route:
            case '/':
                page.views.append(home(page))
            case '/ajuda':
                page.views.append(
                    ft.View(
                        route='/ajuda',
                        controls=[
                            MyAppBar(page, title='Ajuda').build(),
                            ft.ElevatedButton(
                                text='HOME',
                                on_click=lambda _: page.go('/'),
                            ),
                        ],
                    ),
                )
            case '/settings':
                page.views.append(
                    ft.View(
                        route='/settings',
                        controls=[
                            MyAppBar(page, title='Settings').build(),
                            ft.ElevatedButton(
                                text='HOME',
                                on_click=lambda _: page.go('/'),
                            ),
                        ],
                    ),
                )
            case '/exit':
                page.window_destroy()

            case _:
                page.views.append(
                    ft.View(
                        route='/404',
                        vertical_alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            MyAppBar(page, title='Not Found').build(),
                            ft.Text(
                                'Recurso não encontrado!',
                                color='red',
                                weight='bold',
                                text_align=ft.TextAlign.CENTER,
                                size=40,
                            ),
                        ],
                    )
                )
        page.update()

    def view_pop(e: ft.ControlEvent) -> NoReturn:
        """View pop."""
        logging.debug(e)
        page.views.pop()
        page.go(page.views[-1])

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main, view=ft.AppView.FLET_APP_WEB)
