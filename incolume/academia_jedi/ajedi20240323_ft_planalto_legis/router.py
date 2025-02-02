"""Router module."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

__author__ = '@britodfbr'  # pragma: no cover

import logging
from typing import NoReturn

import flet as ft
from views import pages

routes = {'/': pages.splash_vw}


def view_pop(e: ft.ControlEvent) -> NoReturn:
    """View pop."""
    logging.debug(e)
    e.page.views.pop()
    e.page.go(e.page.views[-1])


def route_change(e: ft.RouteChangeEvent) -> NoReturn:
    """Route change."""
    page = e.page
    page.views.clear()
    match page.route:
        case '/':
            page.views.append(pages.home_vw(e))
        case '/ajuda':
            page.views.append(pages.ajuda_vw(e))
        case '/busca':
            page.views.append(pages.busca_vw(e))
        case '/constituicao':
            page.views.append(pages.constituicao_vw(e))
        case '/codigos':
            page.views.append(pages.codigos_vw(e))
        case '/cover':
            page.views.append(pages.splash_vw(e))
        case '/estatutos':
            page.views.append(pages.estatutos_vw(e))
        case '/favoritos':
            page.views.append(pages.favoritos_vw(e))
        case '/resenha':
            page.views.append(pages.resenha_vw(e))
        case '/sobre':
            page.views.append(pages.sobre_vw(e))
        case '/exit':
            page.window_destroy()

        case _:
            page.views.append(pages.not_found_vw(e))
    page.update()
