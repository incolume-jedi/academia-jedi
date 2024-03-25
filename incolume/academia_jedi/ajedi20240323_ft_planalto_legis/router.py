"""Router module."""

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
