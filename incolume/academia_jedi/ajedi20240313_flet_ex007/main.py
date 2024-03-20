"""Nvaigator bar.

baseado em https://youtu.be/ANN0JsiGs40?si=Ntcqe7hqRkoYzGhONvaigator bar.

baseado em https://youtu.be/ANN0JsiGs40?si=Ntcqe7hqRkoYzGhO
"""

import flet as ft
from pathlib import Path
from logging import info

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
    assert imagesdir.is_dir(), f'Ops: {imagesdir=}'
    ft.app(target=main, assets_dir=imagesdir)
