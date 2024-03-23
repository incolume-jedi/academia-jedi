"""Router."""

from typing import NoReturn

import flet as ft
import page_views
from templates import MyAppBar


__author__ = '@britodfbr'  # pragma: no cover


def route_change(e: ft.RouteChangeEvent) -> NoReturn:
    """Route change."""
    page = e.page
    # page.add(ft.Text(f'New route: {e.route}'))
    page.views.clear()
    match page.route:
        case '/':
            page.views.append(page_views.home(page))
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
            page.views.append(page_views.not_found(page))
    page.update()
