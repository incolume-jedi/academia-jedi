"""Exemplo reutilização configuração."""

from typing import NoReturn

import flet as ft

text_field_style = {
    'border_color': ft.colors.AMBER,
    'border_radius': ft.border_radius.all(10),
    'border_width': ft.border.all(width=2),
    'label_style': ft.TextStyle(color=ft.colors.GREEN, italic=True),
}

text_styles = [
    ft.TextStyle(
        color=ft.colors.PRIMARY,
    ),
    ft.TextStyle(
        color=ft.colors.GREEN,
        size=16,
        weight=ft.FontWeight.W_300,
        font_family='Roboto',
    ),
]
hint_styles = [
    ft.TextStyle(
        color=ft.colors.GREEN_300,
        size=16,
    ),
]


def main(page: ft.Page) -> NoReturn:
    """Run it."""
    tf1 = ft.TextField(label='Exemplo 1 - Sem estilo')
    tf2 = ft.TextField(
        label='Exemplo 2 - Com estilo',
        text_style=text_styles[0],
    )
    tf3 = ft.TextField(label='Exemplo 3 - Com estilo', **text_field_style)
    tf4 = ft.TextField(
        label='Exemplo 4 - Com estilo',
        text_style=text_styles[0],
        **text_field_style,
    )
    tf5 = ft.TextField(
        label='Exemplo 4',
        hint_text='Adicione um comentário ..',
        hint_style=hint_styles[0],
        border=ft.InputBorder.UNDERLINE,
        border_color=ft.colors.GREEN_50,
        border_width=1,
        text_style=text_styles[1],
    )

    page.add(tf1, tf2, tf3, tf4, tf5)


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main)
