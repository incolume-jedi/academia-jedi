"""Router."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

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
