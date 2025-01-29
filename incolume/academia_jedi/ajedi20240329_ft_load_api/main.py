"""Module."""

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
