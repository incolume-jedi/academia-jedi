"""Modelo de layout com botões clicáveis.

baseado em https://youtu.be/phEWouTA6JU?si=swBsOtJ1--pmVcuz

to run: flet run examples/ex002
"""

import flet as ft
from logging import info

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
                        # src='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/NASA_logo.svg/110px-NASA_logo.svg.png',
                        src='NASA_logo.svg.png',
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    trailing=ft.Icon(
                        name=ft.icons.MORE_HORIZ,
                        color=ft.colors.BLACK,
                    ),
                ),
                ft.Image(
                    # src='https://upload.wikimedia.org/wikipedia/commons/a/ad/Apollo_15_flag%2C_rover%2C_LM%2C_Irwin_cropped.jpg',
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
