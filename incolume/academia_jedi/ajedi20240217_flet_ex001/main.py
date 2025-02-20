"""Layout de cards.


Tutorial disponível em https://www.youtube.com/watch?v=bV0ux-6L5HA

to run: flet run examples/ex001
"""

import flet as ft

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293


def main(page: ft.Page) -> None:
    """App."""
    page.title = 'Clans of wars'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_min_width = 500
    page.bgcolor = ft.colors.BLACK

    image = ft.Container(
        expand=2,
        clip_behavior=ft.ClipBehavior.NONE,
        border_radius=ft.border_radius.vertical(top=20),
        gradient=ft.LinearGradient(
            begin=ft.alignment.bottom_left,
            end=ft.alignment.top_right,
            colors=[ft.colors.BROWN, ft.colors.SURFACE],
        ),
        content=ft.Image(
            src='Clash-Royale-PNG-Pic.png',
            scale=ft.Scale(scale=1.5),
            width=400,
        ),
    )
    info = ft.Container(
        expand=2,
        padding=ft.padding.all(30),
        alignment=ft.alignment.center,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    value='Level 4',
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.ORANGE,
                ),
                ft.Text(
                    value='Bárbaro',
                    weight=ft.FontWeight.BOLD,
                    size=40,
                    color=ft.colors.BLACK,
                ),
                ft.Text(
                    value='Bárbaros são uma excelente opção para as tropas do'
                    'castelo do clã,'
                    ' pois têm relativamente saúde alta'
                    ' e os danos para o espaço de tropas'
                    ' para habitação individual.'
                    ' Eles são capazes de absorver uma'
                    ' quantidade significativa de dano,'
                    ' atrasando os atacantes e permitindo que'
                    'suas defesas fixas cuidem do resto.',
                    color=ft.colors.GREY,
                    text_align=ft.TextAlign.JUSTIFY,
                ),
            ],
        ),
    )
    skills = ft.Container(
        expand=1,
        bgcolor=ft.colors.ORANGE,
        padding=ft.padding.symmetric(horizontal=20),
        border_radius=ft.border_radius.vertical(bottom=20),
        content=ft.Row(
            controls=[
                ft.Column(
                    expand=1,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            value='20',
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                            size=40,
                        ),
                        ft.Text(
                            value='Defesa',
                            color=ft.colors.WHITE,
                        ),
                    ],
                ),
                ft.VerticalDivider(opacity=0.5),
                ft.Column(
                    expand=1,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            value='16',
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                            size=40,
                        ),
                        ft.Text(
                            value='Velocidade',
                            color=ft.colors.WHITE,
                        ),
                    ],
                ),
                ft.VerticalDivider(opacity=0.5),
                ft.Column(
                    expand=1,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            value='150',
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                            size=40,
                        ),
                        ft.Text(
                            value='Dano',
                            color=ft.colors.WHITE,
                        ),
                    ],
                ),
            ],
        ),
    )

    layout = ft.Container(
        height=700,
        width=400,
        shadow=ft.BoxShadow(blur_radius=100, color=ft.colors.BROWN),
        clip_behavior=ft.ClipBehavior.NONE,
        border_radius=ft.border_radius.all(30),
        bgcolor=ft.colors.WHITE,
        content=ft.Column(
            spacing=0,
            controls=[
                image,
                info,
                skills,
            ],
        ),
    )
    page.add(layout)


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main)
