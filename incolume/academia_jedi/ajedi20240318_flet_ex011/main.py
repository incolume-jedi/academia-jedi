"""Exemplo reutilização configuração."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

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
