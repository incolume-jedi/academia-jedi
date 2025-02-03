"""Settings View."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

from logging import info

import flet as ft


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
