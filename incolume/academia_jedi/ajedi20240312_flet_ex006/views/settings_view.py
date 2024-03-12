"""Settings View."""

import flet as ft
from logging import info


def settingsview(router):
    """Settings View."""
    info('Router: %s', router)

    def toggle_dark_mode(e):
        page = e.page
        if page.theme_mode == 'dark':
            page.theme_mode = 'light'
            page.update()
        else:
            page.theme_mode = 'dark'
            page.update()

    def exit_app(e):
        page = e.page
        page.window_destroy()

    return ft.Column([
        ft.Row(
            [
                ft.Text('My Settings', size=30),
                ft.IconButton(icon=ft.icons.SETTINGS_ROUNDED, icon_size=30),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                ft.TextButton(
                    'Light/Dark Mode',
                    icon=ft.icons.WB_SUNNY_OUTLINED,
                    on_click=toggle_dark_mode,
                ),
            ],
        ),
        ft.Row([
            ft.TextButton(
                'Exit Application',
                icon=ft.icons.CLOSE,
                on_click=exit_app,
                icon_color='red',
            ),
        ]),
    ])
