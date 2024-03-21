"""Roteamento entre páginas."""

from typing import NoReturn

import flet as ft

__author__ = '@britodfbr'  # pragma: no cover


def main(page: ft.Page) -> NoReturn:
    """Run it."""
    page.title = 'sistemas de roteamento'
    page.add(ft.Text(f'Initial route: {page.route}'))

    def route_change(e: ft.RouteChangeEvent):
        """Route change."""
        page.add(ft.Text(f'New route: {e.route}'))
        page.views.clear()
        if page.route == '/':
            page.views.append(
                ft.View(
                    route='/',
                    controls=[
                        ft.AppBar(
                            title=ft.Text('Home'),
                            bgcolor=ft.colors.SURFACE_VARIANT,
                        ),
                        ft.ElevatedButton(
                            text='Loja', on_click=lambda _: page.go('/loja'),
                        ),
                    ],
                ),
            )
        if page.route == '/loja':
            page.views.append(
                ft.View(
                    route='/',
                    controls=[
                        ft.AppBar(
                            title=ft.Text('Loja'),
                            bgcolor=ft.colors.SURFACE_VARIANT,
                        ),
                        ft.ElevatedButton(
                            text='HOME', on_click=lambda _: page.go('/'),
                        ),
                    ],
                ),
            )
        page.update()
        if page.route == '/compras':
            page.views.append(
                ft.View(
                    route='/compras',
                    controls=[
                        ft.AppBar(
                            title=ft.Text('Compras'),
                            bgcolor=ft.colors.SURFACE_VARIANT,
                        ),
                        ft.ElevatedButton(
                            text='HOME', on_click=lambda _: page.go('/'),
                        ),
                    ],
                ),
            )

    def route_compras(e: ft.ControlEvent):
        """Route compras."""
        page.route = '/compras'
        page.update()

    def view_pop(e: ft.ControlEvent) -> NoReturn:
        """View pop."""
        page.views.pop()
        page.go(page.views[-1])

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    # page.update()
    # page.add(ft.ElevatedButton('/compras', on_click=route_compras))


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
