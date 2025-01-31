"""Exemplo Bottom navigator tabs.

baseado em https://www.youtube.com/watch?v=hAWQ5HbDVwA
"""

import flet as ft
from logging import info, debug

__author__ = '@britodfbr'  # pragma: no cover


def main(page: ft.Page) -> None:
    """Main."""
    page.window_width = 280
    page.window_always_on_top = True
    page.scroll = 'always'

    myicons = [
        'home',
        'create',
        'person',
        'settings',
        'favorite',
        'grade',
        'shopping_cart_checkout',
        'expand_circle_down',
    ]
    mylist = ft.Container(
        margin=ft.margin.only(top=page.window_height / 2),
        content=ft.Column(
            [
                ft.Icon(name='home', size=50),
                ft.Text(value='Home app', size=40),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )

    def youchange(e: ft.ControlEvent) -> None:
        """Change content page."""
        idx = e.control.selected_index
        name_screen = e.control.tabs[idx].tab_content.name

        mylist.content.controls[0].name = name_screen
        mylist.content.controls[1].value = f'Tela {name_screen}'
        page.update()

    mytabs = ft.Tabs(
        selected_index=0,
        animation_duration=100,
        indicator_color='write',
        divider_color='green',
        scrollable=True,
        on_change=youchange,
        tabs=[],
    )

    for icon in myicons:
        mytabs.tabs.append(
            ft.Tab(
                tab_content=ft.Icon(
                    name=icon,
                    size=25,
                    color='write',
                ),
            ),
        )

    listnavicon = ft.Container(
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
        ),
        margin=ft.margin.only(top=page.window_height - 100, left=10, right=10),
        border_radius=30,
        width=page.window_width,
        bgcolor='green',
        padding=10,
        content=mytabs,
    )

    def youtaphere(e: ft.ControlEvent) -> None:
        """Quando clica no circulo abre caixa de dialogo."""
        info('Event: %s', e)
        page.dialog = ft.AlertDialog(
            title=ft.Text(value='Open you dialog.', size=30),
            content=ft.Text(value='One example!!'),
            actions=[
                ft.ElevatedButton(
                    text='Close',
                    on_click=lambda _: debug('close'),
                ),
                ft.ElevatedButton(
                    text='test',
                    on_click=lambda _: debug('test'),
                ),
            ],
        )
        page.dialog.open = True
        page.update()

    page.overlay.append(
        ft.Stack(
            controls=[
                ft.ResponsiveRow(
                    col=12,
                    controls=[
                        ft.Column(
                            [listnavicon],
                        ),
                    ],
                ),
                ft.Container(
                    padding=10,
                    margin=ft.margin.only(
                        top=page.window_height - 150,
                        left=page.window_width / 2 - 25,
                        right=page.window_width / 2 - 25,
                    ),
                    bgcolor='green',
                    border=ft.border.all(5, 'write'),
                    shape=ft.BoxShape.CIRCLE,
                    content=ft.GestureDetector(
                        mouse_cursor=ft.MouseCursor.CLICK,
                        on_tap=youtaphere,
                        content=ft.Icon(
                            name='add',
                            size=40,
                            color='write',
                            tooltip='Adding any thing!',
                        ),
                    ),
                ),
            ],
        ),
    )

    page.add(
        ft.Row(
            controls=[mylist],
            alignment='center',
        ),
    )


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main)
