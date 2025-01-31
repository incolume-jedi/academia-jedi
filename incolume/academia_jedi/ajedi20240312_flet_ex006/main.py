"""Main."""

import flet as ft
from views.routes import router
from user_controls.app_bar import navbar


def main(page: ft.Page) -> None:
    """Main."""
    page.theme_mode = 'dark'
    page.appbar = navbar(page)
    page.on_route_change = router.route_change
    router.page = page
    page.add(router.body)
    page.go('/')


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main, assets_dir='assets')
