"""Main module."""

import flet as ft
from pathlib import Path
from time import sleep
import logging

from incolume.academia_jedi.ajedi20240323_ft_planalto_legis.router import (
    route_change,
    view_pop,
)
from incolume.academia_jedi.ajedi20240323_ft_planalto_legis.views.components import (
    set_appbar,
    set_bg,
)
from incolume.academia_jedi.ajedi20240323_ft_planalto_legis.views.pages import (
    set_navbar,
    page_form,
)

assets = Path(__file__).parent / 'assets'
if not assets.is_dir():
    raise FileNotFoundError(f'Ops: {assets=}')
logging.debug(assets)
from incolume.academia_jedi.ajedi20240323_ft_planalto_legis.views import pages


def settings_page(page: ft.Page, *, title: str = '') -> ft.Page:
    """Setting page."""
    page.window_always_on_top = True
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.title = title or 'Planalto Legis'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_min_width = 450
    page.window_min_height = 720
    page.padding = 0
    page.window_width = page.window_min_width
    page.window_height = page.window_min_height
    page.scroll = ft.ScrollMode.ALWAYS
    page.window_bgcolor = ft.colors.BLACK
    return page


def main0(page: ft.Page) -> None:
    """Main proccess."""
    page = settings_page(page)
    logging.debug(page.controls)
    sleep(3.5)
    page.controls.clear()
    page.appbar = set_appbar(page)
    page.navigation_bar = set_navbar(page)
    background = set_bg(page)
    page.add(background)

    sleep(2)
    page.appbar.title = ft.Text('Ops')
    background.controls[1].controls[0].value = 'Ops!!'
    logging.debug(background.controls[1].controls[0])
    page.update()

    # sleep(2)
    # background.controls.pop(-1)
    # background.controls.append(page_about(page))
    # page.update()

    sleep(2)
    page.appbar.title = ft.Text('Busca Avançada')
    background.controls.pop(-1)
    background.controls.append(page_form(page))
    page.update()


def main1(page: ft.Page) -> None:
    """Main proccess."""
    page = settings_page(page)
    page.add(pages.splash_vw)
    page.update()


def main(page: ft.Page) -> None:
    """Main proccess."""
    page = settings_page(page)
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


if __name__ == '__main__':
    ft.app(target=main, assets_dir=assets.as_posix())
