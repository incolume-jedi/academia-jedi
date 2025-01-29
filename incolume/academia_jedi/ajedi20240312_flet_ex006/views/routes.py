"""Rotas."""

from views.data_view import dataview
from views.index_view import indexview
from views.profile_view import profileview
from views.Router import DataStrategyEnum, Router
from views.settings_view import settingsview

router = Router(DataStrategyEnum.QUERY)

router.routes = {
    '/': indexview,
    '/profile': profileview,
    '/settings': settingsview,
    '/data': dataview,
}
