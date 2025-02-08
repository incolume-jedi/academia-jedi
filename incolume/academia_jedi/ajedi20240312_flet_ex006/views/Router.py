"""Router."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

from collections.abc import Callable
from enum import Enum

import flet as ft
from icecream import ic


class DataStrategyEnum(Enum):
    """Data Strategy Enum."""

    QUERY = 0
    ROUTER_DATA = 1
    CLIENT_STORAGE = 2
    STATE = 3


class Router:
    """Router."""

    def __init__(self, data_strategy: DataStrategyEnum = None):
        """Init."""
        self.data_strategy = data_strategy or DataStrategyEnum.QUERY
        self.data = {}
        self.routes = {}
        self.body = ft.Container()

    def set_route(self, stub: str, view: Callable) -> None:
        """Set Route."""
        self.routes[stub] = view

    def set_routes(self, route_dictionary: dict) -> None:
        """Sets multiple routes at once. Ex: {"/": IndexView }."""
        self.routes.update(route_dictionary)

    def route_change(self, route):
        """Route Change."""
        ic(route)
        _page = route.route.split('?')[0]
        queries = route.route.split('?')[1:]
        ic(_page, queries)

        for item in queries:
            key = item.split('=')[0]
            value = item.split('=')[1]
            self.data[key] = value.replace('+', ' ')

        self.body.content = self.routes[_page](self)
        self.body.update()

    def set_data(self, key, value):
        """Set Data."""
        self.data[key] = value

    def get_data(self, key):
        """Get Data."""
        return self.data.get(key)

    def get_query(self, key):
        """Get Query."""
        return self.data.get(key)
