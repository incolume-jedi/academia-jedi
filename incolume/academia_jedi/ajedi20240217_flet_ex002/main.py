"""Modelo de layout com botões clicáveis.

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

baseado em https://youtu.be/phEWouTA6JU?si=swBsOtJ1--pmVcuz

to run: flet run examples/ex002
"""

from logging import info

import flet as ft

__author__ = '@britodfbr'  # pragma: no cover


def main(page: ft.Page) -> None:
    """Main."""
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLACK

    def clicked(e: ft.ControlEvent) -> None:
        """Clicked."""
        e.control.selected = not e.control.selected
        info('%s', e)
        e.control.update()

    layout = ft.Container(
        bgcolor=ft.colors.WHITE,
        width=400,
        border_radius=ft.border_radius.all(10),
        shadow=ft.BoxShadow(blur_radius=50, color=ft.colors.TEAL),
        content=ft.Column(
            spacing=0,
            controls=[
                ft.ListTile(
                    title=ft.Text(
                        value='Nasa',
                        color=ft.colors.BLACK,
                        weight=ft.FontWeight.BOLD,
                    ),
                    subtitle=ft.Text(
                        value='A lua!',
                        color=ft.colors.BLACK,
                    ),
                    leading=ft.Image(
                        src='NASA_logo.svg.png',
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    trailing=ft.Icon(
                        name=ft.icons.MORE_HORIZ,
                        color=ft.colors.BLACK,
                    ),
                ),
                ft.Image(
                    src='Apollo_15_flag_rover_LM_Irwin_cropped.jpg',
                    fit=ft.ImageFit.CONTAIN,
                ),
                ft.Container(
                    padding=ft.padding.all(15),
                    content=ft.Column(
                        controls=[
                            ft.ResponsiveRow(
                                columns=12,
                                vertical_alignment=(
                                    ft.CrossAxisAlignment.CENTER
                                ),
                                controls=[
                                    ft.IconButton(
                                        col=1,
                                        icon=ft.icons.FAVORITE_BORDER,
                                        selected_icon=ft.icons.FAVORITE,
                                        selected=False,
                                        on_click=clicked,
                                        icon_color=ft.colors.BLACK,
                                        selected_icon_color=ft.colors.RED,
                                    ),
                                    ft.Icon(
                                        col=1,
                                        name=ft.icons.CHAT_BUBBLE_OUTLINE,
                                        color=ft.colors.BLACK,
                                    ),
                                    ft.Icon(
                                        col=1,
                                        name=ft.icons.SEND,
                                        color=ft.colors.BLACK,
                                    ),
                                    ft.Container(col=8),
                                    ft.IconButton(
                                        col=1,
                                        icon=ft.icons.BOOKMARK_BORDER,
                                        selected_icon=ft.icons.BOOKMARK_ROUNDED,
                                        selected=False,
                                        on_click=clicked,
                                        icon_color=ft.colors.BLACK,
                                        selected_icon_color=ft.colors.BLACK,
                                    ),
                                ],
                            ),
                            ft.Text(
                                spans=[
                                    ft.TextSpan(
                                        text='Curtido por ',
                                        style=ft.TextStyle(
                                            color=ft.colors.BLACK,
                                            size=16,
                                        ),
                                    ),
                                    ft.TextSpan(
                                        text='Britodfbr ',
                                        style=ft.TextStyle(
                                            color='#000000',
                                            size=16,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                    ),
                                    ft.TextSpan(
                                        text='e ',
                                        style=ft.TextStyle(
                                            color=ft.colors.BLACK,
                                            size=16,
                                        ),
                                    ),
                                    ft.TextSpan(
                                        text='1969 outros.',
                                        style=ft.TextStyle(
                                            color='#000000',
                                            size=16,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                    ),
                                ],
                            ),
                            ft.Text(
                                value='Um pequeno passo para o homem,'
                                ' mas um grande passo '
                                'para humanidade.',
                                color=ft.colors.BLACK,
                                size=16,
                            ),
                            ft.Text(
                                value='55 anos atrás.',
                                color=ft.colors.GREY,
                                size=14,
                                offset=ft.Offset(x=0, y=-0.5),
                            ),
                            ft.Text(
                                spans=[
                                    ft.TextSpan(
                                        text='elonmusk ',
                                        style=ft.TextStyle(
                                            color='#000000',
                                            size=16,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                    ),
                                    ft.TextSpan(
                                        text='Agora bora para marte!! #SpaceX',
                                        style=ft.TextStyle(
                                            color=ft.colors.BLACK,
                                            size=16,
                                        ),
                                    ),
                                ],
                            ),
                            ft.Text(
                                value='Ver outros comentários',
                                color=ft.colors.GREY,
                                size=16,
                                offset=ft.Offset(x=0, y=-0.5),
                            ),
                            ft.TextField(
                                hint_text='Adicione um comentário ..',
                                hint_style=ft.TextStyle(
                                    color=ft.colors.GREY,
                                    size=16,
                                ),
                                border=ft.InputBorder.UNDERLINE,
                                border_color=ft.colors.GREY,
                                border_width=1,
                                color=ft.colors.BLACK,
                            ),
                        ],
                    ),
                ),
            ],
        ),
    )

    page.add(layout)


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main)
