"""Roteamento entre páginas."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

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


def main(page: ft.Page) -> NoReturn:
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
