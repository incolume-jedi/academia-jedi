"""Exemplo menu retratil.

[Forwarded from Programador Aventureiro (Admin)]
Segue o código desse exemplo para referência
"""

from typing import NoReturn

import flet as ft


def main(page: ft.Page) -> NoReturn:
    """Main it."""
    page.bgcolor = ft.colors.BLACK

    def toggle_sidebar(e):
        e.control.content.extended = not e.control.content.extended
        e.control.update()

    sidebar = ft.Container(
        content=ft.NavigationRail(
            bgcolor=ft.colors.BLUE_GREY_900,
            leading=ft.Image(
                src='https://programadoraventureiro.com/wp-content/uploads/'
                '2023/08/Logo-Programador-Aventureiro-100x72.png',
            ),
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.icons.HOME,
                    label='Início',
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.BOOKMARK_BORDER,
                    selected_icon=ft.icons.BOOKMARK,
                    label='Itens salvos',
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.SETTINGS,
                    label='Configurações',
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.LOGOUT,
                    label='Sair',
                ),
            ],
            selected_index=0,
            extended=False,
            label_type=ft.NavigationRailLabelType.NONE,
            on_change=lambda e: print(e.control.selected_index),  # noqa: T201
        ),
        on_hover=toggle_sidebar,
    )

    row = ft.Row(
        controls=[sidebar, ft.Container(bgcolor='amber', expand=True)],
        expand=True,
    )
    page.add(row)


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main, view=ft.AppView.FLET_APP)
