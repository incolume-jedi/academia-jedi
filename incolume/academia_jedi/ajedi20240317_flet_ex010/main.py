"""Exemplo de layout."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

from typing import NoReturn

import flet as ft


class Expense(ft.UserControl):
    """Expense class."""

    def hover_animation(self, e):
        """Hover animation."""
        if e.data == 'true':
            e.control.content.controls[2].offset = ft.transform.Offset(0, 0)
            e.control.content.controls[2].opacity = 100
            e.control.update()

        else:
            e.control.content.controls[2].offset = ft.transform.Offset(0, 1)
            e.control.content.controls[2].opacity = 0
            e.control.update()

    def change_icon(self, e):
        """Change icon."""
        if e.control.selected is not True:
            e.control.selected = True
            e.control.icon_color = 'white'
            e.control.update()
        else:
            e.control.selected = False
            e.control.icon_color = 'white54'
            e.control.update()

    def icon(self, name, color, selected):
        """Icon."""
        return ft.IconButton(
            icon=name,
            icon_size=18,
            icon_color=color,
            selected=selected,
            on_click=lambda e: self.change_icon(e),
        )

    def main_container(self):
        """Main container."""
        self.main = ft.Container(
            width=290,
            height=600,
            bgcolor='black',
            border_radius=35,
            padding=8,
        )

        self.main_col = ft.Column()

        self.green_container = ft.Container(
            width=self.main.width,
            height=self.main.height * 0.45,
            border_radius=30,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=['#0f766e', '#064e3b'],
            ),
        )

        self.notification = self.icon(
            ft.icons.NOTIFICATIONS,
            'white54',
            selected=True,
        )
        self.hide = self.icon(ft.icons.HIDE_SOURCE, 'white54', selected=False)
        self.chat = self.icon(ft.icons.CHAT_ROUNDED, 'white54', selected=False)

        self.icon_column = ft.Column(
            alignment='center',
            spacing=5,
            controls=[
                self.notification,
                self.hide,
                self.chat,
            ],
        )

        self.inner_green_container = ft.Container(
            width=self.green_container.width,
            height=self.green_container.height,
            content=ft.Row(
                spacing=0,
                controls=[
                    ft.Column(
                        expand=4,
                        controls=[
                            ft.Container(
                                padding=20,
                                expand=True,
                                content=ft.Row(
                                    controls=[
                                        ft.Column(
                                            controls=[
                                                ft.Text(
                                                    'Welcome',
                                                    size=10,
                                                    color='white70',
                                                ),
                                                ft.Text(
                                                    'Marcus',
                                                    size=18,
                                                    weight='bold',
                                                ),
                                                ft.Container(
                                                    padding=ft.padding.only(
                                                        top=35,
                                                        bottom=35,
                                                    ),
                                                ),
                                                ft.Text(
                                                    'Total Currence',
                                                    size=10,
                                                    color='white70',
                                                ),
                                                ft.Text(
                                                    '# 11,000.00',
                                                    size=18,
                                                    weight='bold',
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                    ft.Column(
                        expand=1,
                        controls=[
                            ft.Container(
                                padding=ft.padding.only(right=10),
                                expand=True,
                                content=ft.Row(
                                    alignment='center',
                                    controls=[
                                        ft.Column(
                                            alignment='center',
                                            horizontal_alignment='center',
                                            controls=[
                                                ft.Column(
                                                    alignment='center',
                                                    horizontal_alignment='center',
                                                    controls=[
                                                        ft.Container(
                                                            width=40,
                                                            height=150,
                                                            bgcolor='white10',
                                                            border_radius=14,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        )

        self.grid_transfers = ft.GridView(
            expand=True,
            max_extent=150,
            runs_count=0,
            spacing=12,
            run_spacing=5,
            horizontal=True,
        )

        self.grid_payments = ft.GridView(
            expand=True,
            max_extent=150,
            runs_count=0,
            spacing=12,
            run_spacing=5,
        )

        self.main_content_area = ft.Container(
            width=self.main.width,
            height=self.main.height * 0.50,
            bgcolor=ft.colors.SURFACE,
            border_radius=30,
            padding=ft.padding.only(top=10, left=10, right=10),
            content=ft.Column(
                spacing=20,
                controls=[
                    ft.Row(
                        alignment='spaceBetween',
                        vertical_alignment='end',
                        controls=[
                            ft.Container(
                                content=ft.Text(
                                    'Recent',
                                    size=14,
                                    weight='bold',
                                ),
                            ),
                            ft.Container(
                                content=ft.Text(
                                    'View All',
                                    size=10,
                                    weight='w400',
                                    color='white54',
                                ),
                            ),
                        ],
                    ),
                    ft.Container(
                        height=50,
                        content=self.grid_transfers,
                    ),
                    ft.Row(
                        alignment='spaceBetween',
                        vertical_alignment='end',
                        controls=[
                            ft.Container(
                                content=ft.Text(
                                    'Pending',
                                    size=14,
                                    weight='bold',
                                ),
                            ),
                            ft.Container(
                                content=ft.Text(
                                    'View All',
                                    size=10,
                                    weight='w400',
                                    color='white54',
                                ),
                            ),
                        ],
                    ),
                    self.grid_payments,
                ],
            ),
        )

        info_list = ['PH', 'SD', 'WQ', 'KG', 'TY', 'SB', 'LP', 'LK']
        for i in info_list:
            __ = ft.Container(
                width=100,
                height=100,
                bgcolor='white10',
                border_radius=15,
                alignment=ft.alignment.center,
                content=ft.Text(f'{i}', weight='bold'),
            )

            self.grid_transfers.controls.append(__)

        payment_list = [
            ['Utilities', '$ 523.23'],
            ['Phone', '$ 102.23'],
            ['Insurance', '$ 128.23'],
            ['Gas', '$ 23.23'],
            ['Groceries', '$ 289.23'],
            ['Documents', '$ 77.23'],
        ]
        for i in payment_list:
            __ = ft.Container(
                width=100,
                height=100,
                bgcolor='white10',
                border_radius=15,
                alignment=ft.alignment.center,
                content=ft.Text(f'{i}', weight='bold'),
                on_hover=lambda e: self.hover_animation(e),
            )

            self.grid_payments.controls.append(__)

            for _ in i:
                __.content = ft.Column(
                    alignment='center',
                    horizontal_alignment='center',
                    controls=[
                        ft.Text(f'{i[0]}', size=11, color='white54'),
                        ft.Text(f'{i[1]}', size=16, weight='bold'),
                        #
                        ft.Text(
                            'Pay Now?',
                            color='white60',
                            size=12,
                            text_align='start',
                            weight='w600',
                            offset=ft.transform.Offset(0, 1),
                            animate_offset=ft.animation.Animation(
                                duration=900,
                                curve='decelerate',
                            ),
                            animate_opacity=300,
                            opacity=0,
                        ),
                    ],
                )

        self.green_container.content = self.inner_green_container

        self.main_col.controls.append(self.green_container)
        self.main_col.controls.append(self.main_content_area)

        self.main.content = self.main_col

        for icon in self.icon_column.controls[:]:
            if icon.selected is True:
                icon.icon_color = 'white'

        return self.main

    def build(self):
        """Builder class."""
        return ft.Column(
            controls=[
                self.main_container(),
            ],
        )


def start(page: ft.Page) -> NoReturn:
    """Run it."""
    page.title = 'Flet Exp'
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    app = Expense()
    page.add(app)


if __name__ == '__main__':
    ft.app(target=start)
