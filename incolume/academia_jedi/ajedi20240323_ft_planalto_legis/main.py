"""Main module."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

import logging
from pathlib import Path
from time import sleep

import flet as ft

from incolume.academia_jedi.ajedi20240323_ft_planalto_legis.router import (
    route_change,
    view_pop,
)
from incolume.academia_jedi.ajedi20240323_ft_planalto_legis.views import pages
from incolume.academia_jedi.ajedi20240323_ft_planalto_legis.views.components import (
    set_appbar,
    set_bg,
)
from incolume.academia_jedi.ajedi20240323_ft_planalto_legis.views.pages import (
    page_form,
    set_navbar,
)

assets = Path(__file__).parent / 'assets'
if not assets.is_dir():
    raise FileNotFoundError(f'Ops: {assets=}')
logging.debug(assets)


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
