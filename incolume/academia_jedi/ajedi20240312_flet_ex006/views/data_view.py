"""Data View."""

from typing import Union

import flet as ft
from State import global_state
from views.Router import DataStrategyEnum, Router


def dataview(router: Union[Router, str, None] = None) -> None:
    """Data View."""
    text = ft.Text('')

    if router and router.data_strategy == DataStrategyEnum.QUERY:
        text = ft.Text('Query Data: ' + router.get_query('data'))
    elif router and router.data_strategy == DataStrategyEnum.ROUTER_DATA:
        text = ft.Text('Router Data: ' + router.get_data('data'))
    elif router and router.data_strategy == DataStrategyEnum.CLIENT_STORAGE:
        text = ft.Text(
            'Client Storage: ' + router.page.client_storage.get('data'),
        )
    elif router and router.data_strategy == DataStrategyEnum.STATE:
        text = ft.Text(
            'State: ' + global_state.get_state_by_key('data').get_state(),
        )
    return ft.Column([
        ft.Row(
            [
                ft.Text('Data View', size=50),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    ])
