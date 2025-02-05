"""Timer."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

import ast
from logging import info
from time import sleep

import flet as ft


def main(page: ft.Page) -> None:
    """Main."""
    page.title = 'Timer App'
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.theme_mode = 'dark'
    page.padding = 40
    page.window_frameless = True
    page.window_height = 490
    page.window_width = 490

    seconds = ft.TextField(
        hint_text='seconds...',
        border_radius=30,
        width=120,
        text_align='center',
    )

    def start_timer(e: ft.ControlEvent) -> None:
        button.visible = False
        sec_value = int(ast.literal_eval(seconds.value))
        while sec_value:
            mins, secs = divmod(sec_value, 60)
            time.value = f'{mins:02d} min {secs:02d} sec'
            sleep(1)
            sec_value = sec_value - 1
            page.update()
        sleep(1)
        time.value = f'{mins:02d} min {sec_value:02d} sec'
        button.visible = True
        info('%s', e)
        page.update()

    time = ft.Text(style='displayLarge', color='white')
    button = ft.ElevatedButton(
        'set timer',
        on_click=start_timer,
        color='green',
    )

    page.add(
        ft.Image(src='logo.png', height=90),
        ft.Container(padding=20),
        ft.Row([seconds, button], alignment='center'),
        ft.Container(padding=20),
        time,
        ft.Container(padding=20),
        ft.Text(
            'Designed and Developed by: kmranrg (Instagram)',
            color='yellow',
        ),
    )


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main, assets_dir='assets')
