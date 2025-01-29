"""Index View."""

import flet as ft
from views.Router import DataStrategyEnum, Router


def indexview(router_data: Router | str | None = None) -> None:  # noqa: C901
    """Index View."""

    def send_data(e: ft.ControlEvent) -> None:  # noqa: C901
        if text_field.value == '':
            return
        if router_data and router_data.data_strategy == DataStrategyEnum.QUERY:
            e.page.go('/data', data=text_field.value)
        elif (
            router_data
            and router_data.data_strategy == DataStrategyEnum.ROUTER_DATA
        ):
            router_data.set_data('data', text_field.value)
            e.page.go('/data', data=text_field.value)
        elif (
            router_data
            and router_data.data_strategy == DataStrategyEnum.CLIENT_STORAGE
        ):
            e.page.client_storage.set('data', text_field.value)
            e.page.go('/data')
        elif (
            router_data and router_data.data_strategy == DataStrategyEnum.STATE
        ):
            e.page.go('/data')
        else:
            e.page.go('/data')

    text_field = ft.TextField()
    send_button = ft.ElevatedButton('Send')
    send_button.on_click = send_data
    return ft.Column([
        ft.Row(
            [
                ft.Text('Welcome to my Flet Router Tutorial', size=50),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [text_field, send_button],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    ])
