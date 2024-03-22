"""Roteamento entre páginas."""

import logging
from typing import NoReturn, Any

import flet as ft

__author__ = '@britodfbr'  # pragma: no cover


class MyAppBar(ft.UserControl):
    """Appbar personalizado."""

    def __init__(
        self,
        page: ft.Page,
        title: str = '',
        *args: Any,
        **kwargs: Any,
    ):
        """Init it."""
        super().__init__(*args, **kwargs)
        self.page = page
        self.title = title or 'Home'

    def build(self):
        """Build it."""
        return ft.AppBar(
            title=ft.Text(self.title),
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(
                            text='Home',
                            on_click=lambda _: self.page.go('/'),
                        ),
                        ft.PopupMenuItem(
                            text='loja',
                            on_click=lambda _: self.page.go('/loja'),
                        ),
                        ft.PopupMenuItem(
                            text='settings',
                            on_click=lambda _: self.page.go('/settings'),
                        ),
                    ],
                ),
            ],
        )

    def __call__(self, *args: Any, **kwargs: Any) -> ft.AppBar:
        """Call it."""
        logging.debug('args: %s', args)
        logging.debug('kwargs: %s', kwargs)
        return self.build()


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
                page.views.append(
                    ft.View(
                        route='/',
                        controls=[
                            MyAppBar(page).build(),
                            ft.Text('Homepage'),
                        ],
                    ),
                )
            case '/loja':
                page.views.append(
                    ft.View(
                        route='/',
                        controls=[
                            MyAppBar(page, title='Loja').build(),
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
            case _:
                page.update()
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
