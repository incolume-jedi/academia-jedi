"""Nvaigator bar.

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

baseado em https://youtu.be/ANN0JsiGs40?si=Ntcqe7hqRkoYzGhONvaigator bar.

baseado em https://youtu.be/ANN0JsiGs40?si=Ntcqe7hqRkoYzGhO
"""

from logging import info
from pathlib import Path

import flet as ft

width: float = 720 * 1.6
height: float = 405 * 1.6


class MenuButton(ft.UserControl):
    """Class MenuButton."""

    def __init__(self, icon, text, width, hover_color):
        """Init MenuButton."""
        super().__init__()
        self.icon = icon
        self.text = text
        self.width = width
        self.hover_color = hover_color
        self.button = ft.Container(
            width=width,
            content=ft.Row(
                controls=[
                    ft.Icon(self.icon, color='white'),
                    ft.Text(self.text, color='white', size=16, weight='w600'),
                ],
            ),
            bgcolor='transparent',
            blur=ft.Blur(12, 12, ft.BlurTileMode.MIRROR),
            on_hover=self.hover,
        )

    def hover(self, e):
        """Hover."""
        info('Event: %s', e)
        self.button.bgcolor = self.hover_color

    def build(self):
        """Build MednuButton."""
        return self.button


class SideBar(ft.UserControl):
    """SideBar."""

    def __init__(self, *args, **kwargs):
        """Init."""
        super().__init__(*args, **kwargs)
        self.bgcolor = '#44000000'
        self.menubar = ft.GestureDetector(
            ft.Container(
                ft.Row(
                    controls=[
                        ft.Container(
                            width=10,
                            height=10,
                            border_radius=360,
                            bgcolor='red',
                        ),
                        ft.Container(
                            width=10,
                            height=10,
                            border_radius=360,
                            bgcolor='yellow',
                        ),
                        ft.Container(
                            width=10,
                            height=10,
                            border_radius=360,
                            bgcolor='green',
                        ),
                    ],
                ),
                height=40,
                width=300,
                padding=ft.padding.only(20, 10, 0, 10),
                bgcolor=self.bgcolor,
                blur=ft.Blur(12, 12, ft.BlurTileMode.MIRROR),
            ),
            on_pan_update=self.update_pos,
        )

        self.body = ft.Container(
            width=300,
            height=500,
            content=ft.Column(
                controls=[
                    self.menubar,
                    ft.Container(
                        content=ft.Text(
                            'Menu',
                            color='#111111',
                            size=16,
                            weight='w500',
                        ),
                        padding=ft.padding.only(left=20),
                    ),
                    ft.Container(
                        padding=ft.padding.only(left=20),
                        content=ft.Column(
                            controls=[
                                MenuButton(
                                    ft.icons.DASHBOARD_CUSTOMIZE_OUTLINED,
                                    'Dashboard',
                                    240,
                                    self.bgcolor,
                                ),
                            ],
                        ),
                    ),
                ],
            ),
            left=50,
            top=50,
            border_radius=6,
            bgcolor=self.bgcolor,
            blur=ft.Blur(12, 12, ft.BlurTileMode.MIRROR),
        )

    def update_pos(self, e):
        """Update position."""
        self.body.top = max(0, self.body.top + e.delta_y)
        self.body.left = max(0, self.body.left + e.delta_x)
        self.body.update()

    def build(self):
        """Build."""
        return self.body


body = ft.Container(
    content=ft.Stack(
        controls=[
            ft.Image(
                src=Path('images', 'background.jpg').as_posix(),
                width=width,
                height=height,
                left=0,
                top=0,
            ),
            SideBar(),
        ],
    ),
    width=width,
    height=height,
)


def main(page: ft.Page) -> None:
    """Main."""
    page.window_max_width = width
    page.window_max_height = height
    page.window_width = width
    page.window_height = height
    page.window_resizable = False
    page.padding = 0
    page.add(body)


if __name__ == '__main__':
    imagesdir = Path(__file__).resolve().parent.joinpath('assets')
    if not imagesdir.is_dir():
        raise FileNotFoundError(f'Ops: {imagesdir=}')
    ft.app(target=main, assets_dir=imagesdir)
