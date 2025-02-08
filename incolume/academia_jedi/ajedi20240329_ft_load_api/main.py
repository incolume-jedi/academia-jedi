"""Module."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

__author__ = '@britodfbr'  # pragma: no cover

import datetime as dt
import logging
from dataclasses import dataclass, field
from time import sleep
from typing import Any, NoReturn

import flet as ft
import httpx
from icecream import ic

logging.basicConfig(
    format='%(asctime)s;%(levelname)-8s;%(name)s;%(module)s;%(funcName)s;%(message)s',
    level=logging.INFO,
)


@dataclass
class Person:
    """Class person."""

    name: str
    height: float = ''
    mass: float = ''
    hair_color: str = ''
    skin_color: str = ''
    eye_color: str = ''
    birth_year: str = ''
    gender: str = ''
    homeworld: str = ''
    films: list[str] = field(default_factory=list, repr=False)
    species: list[str] = field(default_factory=list, repr=False)
    vehicles: list[str] = field(default_factory=list, repr=False)
    starships: list[str] = field(default_factory=list, repr=False)
    created: dt.datetime = field(default_factory=dt.datetime.now)
    edited: dt.datetime = field(default_factory=dt.datetime.now)
    url: str = ''


class PersonModel:
    """Modelo person."""

    people = None

    def __init__(self):
        """Init from PersonModel."""
        self.data: list[dict[str, Any]] = []
        self._get_people()

    def _get_people(self):
        """Get person from API swapi.dev."""
        url = 'https://swapi.dev/api/people/'
        try:
            while url is not None:
                logging.info('url=%s', url)
                ic(url)
                response = httpx.get(url)
                self.data += response.json().get('results')
                url = response.json().get('next')
        except AttributeError:
            logging.exception('Total de páginas atingido..')
            raise

        return self.data

    @property
    def quantia(self) -> int:
        """Quantia total registrada."""
        return len(self.people) if self.people else 0

    def get_all(self):
        """Get all results."""
        if not self.people:
            self.people = (Person(**p) for p in self.data)
        return self.people


def main(page: ft.Page) -> NoReturn:
    """Run it."""
    page.scroll = ft.ScrollMode.AUTO
    people = PersonModel()
    content = ft.ListView(spacing=15, auto_scroll=True, padding=10)
    sleep(5)
    for person in people.get_all():
        ic(person)
        element = ft.Container(
            content=ft.ResponsiveRow(
                controls=[
                    ft.Text(
                        col=6,
                        value=person.name,
                        weight='bold',
                        size=15,
                    ),
                    ft.Text(col=2, value=person.gender),
                    ft.Text(col=2, value=person.gender),
                    ft.Text(col=2, value=person.gender),
                ],
            ),
        )
        content.controls.append(element)

    page.add(content)


def run():
    """Pseudo test."""
    people = PersonModel()
    # print(people.get_people())
    ic(people.get_all(), people.quantia)


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main)
    # run()
