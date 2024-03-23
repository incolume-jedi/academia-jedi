"""Router."""

from typing import NoReturn

import flet as ft
import page_views


__author__ = '@britodfbr'  # pragma: no cover


def route_change(e: ft.RouteChangeEvent) -> NoReturn:
    """Route change."""
    page = e.page
    page.views.clear()
    match page.route:
        case '/':
            page.views.append(page_views.home(page))
        case '/ajuda':
            page.views.append(page_views.vw_help(page))
        case '/busca-avancada':
            page.views.append(page_views.busca_avancada(page))
        case '/constituicao':
            page.views.append(page_views.constituicao(page))
        case '/codigos':
            page.views.append(page_views.codigos(page))
        case '/estatutos':
            page.views.append(page_views.estatutos(page))
        case '/favoritos':
            page.views.append(page_views.favoritos(page))
        case '/resenha':
            page.views.append(page_views.resenha(page))
        case '/settings':
            page.views.append(page_views.settings(page))
        case '/exit':
            page.window_destroy()

        case _:
            page.views.append(page_views.not_found(page))
    page.update()
