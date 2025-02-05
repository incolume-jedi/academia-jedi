"""Advanced To Do App."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

from logging import info

import flet as ft
from custom_checkbox import CustomCheckBox


def main(page: ft.Page) -> None:
    """Main."""
    bg = '#041955'
    fg = '#3450a1'
    pink = '#eb06ff'

    circle = ft.Stack(
        controls=[
            ft.Container(
                width=100,
                height=100,
                border_radius=50,
                bgcolor='white12',
            ),
            ft.Container(
                gradient=ft.SweepGradient(
                    center=ft.alignment.center,
                    start_angle=0.0,
                    end_angle=3,
                    stops=[0.5, 0.5],
                    colors=['#00000000', pink],
                ),
                width=100,
                height=100,
                border_radius=50,
                content=ft.Row(
                    alignment='center',
                    controls=[
                        ft.Container(
                            padding=ft.padding.all(5),
                            bgcolor=bg,
                            width=90,
                            height=90,
                            border_radius=50,
                            content=ft.Container(
                                bgcolor=fg,
                                height=80,
                                width=80,
                                border_radius=40,
                                content=ft.CircleAvatar(
                                    opacity=0.8,
                                    foreground_image_url='https://images.unsplash.com/photo-1545912452-8aea7e25a3d3?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fgVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
                                ),
                            ),
                        ),
                    ],
                ),
            ),
        ],
    )

    def shrink(e):
        info('Event: %s', e)
        page_2.controls[0].width = 120
        page_2.controls[0].scale = ft.transform.Scale(
            0.8,
            alignment=ft.alignment.center_right,
        )
        page_2.controls[0].border_radius = ft.border_radius.only(
            topLeft=35,
            topRight=0,
            bottomLeft=35,
            bottomRight=0,
        )
        page_2.update()

    def restore(e):
        info('Event: %s', e)
        page_2.controls[0].width = 400
        page_2.controls[0].border_radius = 35
        page_2.controls[0].scale = ft.transform.Scale(
            1,
            alignment=ft.alignment.center_right,
        )
        page_2.update()

    create_task_view = ft.Container(
        content=ft.Container(
            on_click=lambda _: page.go('/'),
            height=40,
            width=40,
            content=ft.Text('x'),
        ),
    )

    tasks = ft.Column(
        height=400,
        scroll='auto',
    )
    for i in range(10):
        info('Loop control: %s', i)
        tasks.controls.append(
            ft.Container(
                height=70,
                width=400,
                bgcolor=bg,
                border_radius=25,
                padding=ft.padding.only(
                    left=20,
                    top=25,
                ),
                content=CustomCheckBox(
                    color=pink,
                    label='Create interesting content!',
                ),
            ),
        )

    categories_card = ft.Row(scroll='auto')
    categories = ['Business', 'Family', 'Friends']
    for i, category in enumerate(categories):
        categories_card.controls.append(
            ft.Container(
                border_radius=20,
                bgcolor=bg,
                width=170,
                height=110,
                padding=15,
                content=ft.Column(
                    controls=[
                        ft.Text('40 Tasks'),
                        ft.Text(category),
                        ft.Container(
                            width=160,
                            height=5,
                            bgcolor='white12',
                            border_radius=20,
                            padding=ft.padding.only(right=i * 30),
                            content=ft.Container(
                                bgcolor=pink,
                            ),
                        ),
                    ],
                ),
            ),
        )

    first_page_contents = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    alignment='spaceBetween',
                    controls=[
                        ft.Container(
                            on_click=lambda e: shrink(e),
                            content=ft.Icon(ft.icons.MENU),
                        ),
                        ft.Row(
                            controls=[
                                ft.Icon(ft.icons.SEARCH),
                                ft.Icon(ft.icons.NOTIFICATIONS_OUTLINED),
                            ],
                        ),
                    ],
                ),
                ft.Container(height=20),
                ft.Text(value="What's up, Olivia!"),
                ft.Text(value='CATEGORIES'),
                ft.Container(
                    padding=ft.padding.only(
                        top=10,
                        bottom=20,
                    ),
                    content=categories_card,
                ),
                ft.Container(height=20),
                ft.Text("TODAY'S TASKS"),
                ft.Stack(
                    controls=[
                        tasks,
                        ft.FloatingActionButton(
                            bottom=2,
                            right=20,
                            icon=ft.icons.ADD,
                            on_click=lambda _: page.go('/create_task'),
                        ),
                    ],
                ),
            ],
        ),
    )

    page_1 = ft.Container(
        width=400,
        height=850,
        bgcolor=bg,
        border_radius=35,
        padding=ft.padding.only(left=50, top=60, right=200),
        content=ft.Column(
            controls=[
                ft.Row(
                    alignment='end',
                    controls=[
                        ft.Container(
                            border_radius=25,
                            padding=ft.padding.only(
                                top=13,
                                left=13,
                            ),
                            height=50,
                            width=50,
                            border=ft.border.all(color='white', width=1),
                            on_click=lambda e: restore(e),
                            content=ft.Text('<'),
                        ),
                    ],
                ),
                ft.Container(height=20),
                circle,
                ft.Text('Olivia\nMitchel', size=32, weight='bold'),
                ft.Container(height=25),
                ft.Row(
                    controls=[
                        ft.Icon(
                            ft.icons.FAVORITE_BORDER_SHARP,
                            color='white60',
                        ),
                        ft.Text(
                            'Templates',
                            size=15,
                            weight=ft.FontWeight.W_300,
                            color='white',
                            font_family='poppins',
                        ),
                    ],
                ),
                ft.Container(height=5),
                ft.Row(
                    controls=[
                        ft.Icon(ft.icons.CARD_TRAVEL, color='white60'),
                        ft.Text(
                            'Templates',
                            size=15,
                            weight=ft.FontWeight.W_300,
                            color='white',
                            font_family='poppins',
                        ),
                    ],
                ),
                ft.Container(height=5),
                ft.Row(
                    controls=[
                        ft.Icon(ft.icons.CALCULATE_OUTLINED, color='white60'),
                        ft.Text(
                            'Templates',
                            size=15,
                            weight=ft.FontWeight.W_300,
                            color='white',
                            font_family='poppins',
                        ),
                    ],
                ),
                ft.Image(
                    src='/images/1.png',
                    width=300,
                    height=200,
                ),
                ft.Text(
                    'Good',
                    color=fg,
                    font_family='poppins',
                ),
                ft.Text(
                    'Consistency',
                    size=22,
                ),
            ],
        ),
    )

    page_2 = ft.Row(
        alignment='end',
        controls=[
            ft.Container(
                width=400,
                height=850,
                bgcolor=fg,
                border_radius=35,
                animate=ft.animation.Animation(
                    600,
                    ft.AnimationCurve.DECELERATE,
                ),
                animate_scale=ft.animation.Animation(400, curve='decelerate'),
                padding=ft.padding.only(top=50, left=20, right=20, bottom=5),
                content=ft.Column(controls=[first_page_contents]),
            ),
        ],
    )

    container = ft.Container(
        width=400,
        height=850,
        bgcolor=bg,
        border_radius=35,
        content=ft.Stack(
            controls=[
                page_1,
                page_2,
            ],
        ),
    )

    pages = {
        '/': ft.View(
            '/',
            [container],
        ),
        '/create_task': ft.View(
            '/create_task',
            [create_task_view],
        ),
    }

    def route_change(route):
        info('Router: %s', route)
        page.views.clear()
        page.views.append(pages[page.route])

    page.on_route_change = route_change
    page.go(page.route)


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main, assets_dir='assets')
