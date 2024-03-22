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
                            text='Busca Avançada',
                            on_click=lambda _: self.page.go('/busca-avancada'),
                        ),
                        ft.PopupMenuItem(
                            text='Constituição',
                            on_click=lambda _: self.page.go('/constituicao'),
                        ),
                        ft.PopupMenuItem(
                            text='Códigos',
                            on_click=lambda _: self.page.go('/codigos'),
                        ),
                        ft.PopupMenuItem(
                            text='Estatutos',
                            on_click=lambda _: self.page.go('/estatutos'),
                        ),
                        ft.PopupMenuItem(
                            text='Favoritos',
                            on_click=lambda _: self.page.go('/favoritos'),
                        ),
                        ft.PopupMenuItem(
                            text='Resenha',
                            on_click=lambda _: self.page.go('/resenha'),
                        ),
                        ft.PopupMenuItem(
                            text='Ajuda',
                            on_click=lambda _: self.page.go('/ajuda'),
                        ),
                        ft.PopupMenuItem(
                            text='Settings',
                            on_click=lambda _: self.page.go('/settings'),
                        ),
                        ft.PopupMenuItem(
                            text='Fechar',
                            icon=ft.icons.CLOSE_ROUNDED,
                            on_click=lambda _: self.page.go('/exit'),
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
                            ft.Text('Recurso não encontrado!', color='red', weight='bold', text_align=ft.TextAlign.CENTER, size=40),

                        ]
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
