"""Module."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

import json
from typing import NoReturn

import flet as ft

__author__ = '@britodfbr'  # pragma: no cover

import httpx


def get_content(url_api: str = '', url_content: str = '') -> dict:
    """Get content from API."""
    url_api = url_api or 'https://httpbin.org/anything'
    url_content = (
        url_content or 'https://loripsum.net/api/10/short/headers/plaintext'
    )
    resp = httpx.get(url_content)
    result = httpx.post(url_api, data=json.dumps(resp.text.split('\n\n')))
    return result.json()


conteudo = get_content()


class MyView(ft.UserControl):
    """View personalizado."""

    def __init__(self, *args, **kwargs):
        """Myview init."""
        super().__init__(*args, **kwargs)

    def build(self):
        """Build Myview."""
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(
                        selectable=True,
                        value=content,
                        text_align=ft.TextAlign.JUSTIFY,
                    )
                    for content in json.loads(conteudo.get('data'))
                ],
            ),
        )


def main(page: ft.Page) -> NoReturn:
    """Run it."""
    page.scroll = 'auto'
    page.add(MyView())


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main)
