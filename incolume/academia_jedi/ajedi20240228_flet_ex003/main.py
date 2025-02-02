"""Exemplo Bottom navigator tabs.

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

baseado em https://www.youtube.com/watch?v=hAWQ5HbDVwA
"""

from logging import debug, info

import flet as ft

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
