"""Router."""

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
