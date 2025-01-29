"""Timer."""

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
