"""Rotas."""

from views.Router import Router, DataStrategyEnum
from views.index_view import indexview
from views.profile_view import profileview
from views.settings_view import settingsview
from views.data_view import dataview

router = Router(DataStrategyEnum.QUERY)

router.routes = {
    '/': indexview,
    '/profile': profileview,
    '/settings': settingsview,
    '/data': dataview,
}
