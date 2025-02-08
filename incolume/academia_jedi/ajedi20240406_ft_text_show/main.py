"""Module."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
# ruff: noqa: E501

__author__ = '@britodfbr'  # pragma: no cover

from typing import NoReturn

import flet as ft


def main(page: ft.Page) -> NoReturn:
    """Run it."""
    page.title = 'Text custom styles'
    page.scroll = 'adaptive'

    page.add(
        ft.Text('Size 10', size=10),
        ft.Text('Size 30, Italic', size=30, color='pink600', italic=True),
        ft.Text(
            'Size 40, w100',
            size=40,
            color=ft.colors.WHITE,
            bgcolor=ft.colors.BLUE_600,
            weight=ft.FontWeight.W_100,
        ),
        ft.Text(
            'Size 50, Normal',
            size=50,
            color=ft.colors.WHITE,
            bgcolor=ft.colors.ORANGE_800,
            weight=ft.FontWeight.NORMAL,
        ),
        ft.Text(
            'Size 60, Bold, Italic',
            size=50,
            color=ft.colors.WHITE,
            bgcolor=ft.colors.GREEN_700,
            weight=ft.FontWeight.BOLD,
            italic=True,
        ),
        ft.Text(
            'Size 70, w900, selectable',
            size=70,
            weight=ft.FontWeight.W_900,
            selectable=True,
        ),
        ft.Text(
            'Limit long text to 1 line with ellipsis',
            theme_style=ft.TextThemeStyle.HEADLINE_SMALL,
        ),
        ft.Text(
            'Proin rutrum, purus sit amet elementum volutpat, nunc lacus vulputate orci, cursus ultrices neque dui quis purus. Ut ultricies purus nec nibh bibendum, eget vestibulum metus varius. Duis convallis maximus justo, eu rutrum libero maximus id. Donec ullamcorper arcu in sapien molestie, non pellentesque tellus pellentesque. Nulla nec tristique ex. Maecenas euismod nisl enim, a convallis arcu laoreet at. Ut at tortor finibus, rutrum massa sit amet, pulvinar velit. Phasellus diam lorem, viverra vitae leo vitae, consequat suscipit lorem.',
            max_lines=1,
            overflow='ellipsis',
        ),
        ft.Text(
            'Limit long text to 2 lines and fading',
            theme_style=ft.TextThemeStyle.HEADLINE_SMALL,
        ),
        ft.Text(
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur quis nibh vitae purus consectetur facilisis sed vitae ipsum. Quisque faucibus sed nulla placerat sagittis. Phasellus condimentum risus vitae nulla vestibulum auctor. Curabitur scelerisque, nibh eget imperdiet consequat, odio ante tempus diam, sed volutpat nisl erat eget turpis. Sed viverra, diam sit amet blandit vulputate, mi tellus dapibus lorem, vitae vehicula diam mauris placerat diam. Morbi sit amet pretium turpis, et consequat ligula. Nulla velit sem, suscipit sit amet dictum non, tincidunt sed nulla. Aenean pellentesque odio porttitor sagittis aliquam. Nam varius at metus vitae vulputate. Praesent faucibus nibh lorem, eu pretium dolor dictum nec. Phasellus eget dui laoreet, viverra magna vitae, pellentesque diam.',
            max_lines=2,
        ),
        ft.Text(
            'Limit the width and height of long text',
            theme_style=ft.TextThemeStyle.HEADLINE_SMALL,
        ),
        ft.Text(
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur quis nibh vitae purus consectetur facilisis sed vitae ipsum. Quisque faucibus sed nulla placerat sagittis. Phasellus condimentum risus vitae nulla vestibulum auctor. Curabitur scelerisque, nibh eget imperdiet consequat, odio ante tempus diam, sed volutpat nisl erat eget turpis. Sed viverra, diam sit amet blandit vulputate, mi tellus dapibus lorem, vitae vehicula diam mauris placerat diam. Morbi sit amet pretium turpis, et consequat ligula. Nulla velit sem, suscipit sit amet dictum non, tincidunt sed nulla. Aenean pellentesque odio porttitor sagittis aliquam. Nam varius at metus vitae vulputate. Praesent faucibus nibh lorem, eu pretium dolor dictum nec. Phasellus eget dui laoreet, viverra magna vitae, pellentesque diam.',
            width=700,
            height=100,
        ),
        ft.Text(
            'Limit the width and height of long text',
            theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM,
            color='red',
        ),
        ft.Text(
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur quis nibh vitae purus consectetur facilisis sed vitae ipsum. Quisque faucibus sed nulla placerat sagittis. Phasellus condimentum risus vitae nulla vestibulum auctor. Curabitur scelerisque, nibh eget imperdiet consequat, odio ante tempus diam, sed volutpat nisl erat eget turpis. Sed viverra, diam sit amet blandit vulputate, mi tellus dapibus lorem, vitae vehicula diam mauris placerat diam. Morbi sit amet pretium turpis, et consequat ligula. Nulla velit sem, suscipit sit amet dictum non, tincidunt sed nulla. Aenean pellentesque odio porttitor sagittis aliquam. Nam varius at metus vitae vulputate. Praesent faucibus nibh lorem, eu pretium dolor dictum nec. Phasellus eget dui laoreet, viverra magna vitae, pellentesque diam.',
        ),
    )


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main)
