"""Roteamento entre páginas."""

from typing import NoReturn, Self

import flet as ft

__author__ = '@britodfbr'  # pragma: no cover


class MyAppBar(ft.UserControl):
    """Class appbar."""

    def __init__(
        self,
        page: ft.Page,
        title: str = '',
        *args: str,
        **kwargs: str,
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

    def __call__(self) -> Self:
        """On call this."""
        return self.build()


def main(page: ft.Page) -> NoReturn:  # noqa: C901
    """Run it."""
    page.title = 'sistemas de roteamento'
    page.add(ft.Text(f'Initial route: {page.route}'))

    def route_change(e: ft.RouteChangeEvent) -> NoReturn:
        """Route change."""
        page.add(ft.Text(f'New route: {e.route}'))
        page.views.clear()
        if page.route == '/':
            page.views.append(
                ft.View(
                    route='/',
                    controls=[
                        MyAppBar(page).build(),
                        ft.Text('Homepage'),
                    ],
                ),
            )
        if page.route == '/loja':
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
        if page.route == '/settings':
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
        page.update()

    def route_compras(_: ft.ControlEvent) -> NoReturn:
        """Route compras."""
        page.route = '/compras'
        page.update()

    def view_pop(_: ft.ControlEvent) -> NoReturn:
        """View pop."""
        page.views.pop()
        page.go(page.views[-1])

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main, view=ft.AppView.FLET_APP_WEB)
