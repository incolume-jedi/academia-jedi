"""Main module."""

__author__ = '@britodfbr'  # pragma: no cover

# ruff: noqa: ANN001, D101, D102, D107
import json
from dataclasses import dataclass
from pathlib import Path

from icecream import ic
from incolume.academia_jedi.ajedi20221109_pony_orm.tratativa1.model import (
    db,
    get_model_municipios,
)
from pony import orm

with (
    Path(__file__)
    .parents[4]
    .joinpath(
        'data_files',
        'json',
        'municipios_br.json',
    )
    .open() as f
):
    municipios = json.load(f)


@dataclass
class MunicipioAPI:
    def __init__(self, db, orm) -> None:
        self.db = db
        self.orm = orm

    def add(self, **kwargs):
        with orm.db_session:
            new_municipio = get_model_municipios(self.db, self.orm)
            new_municipio(
                CODIGO_MUNICIPIO=kwargs.get('CODIGO_MUNICIPIO'),
                NOME_MUNICIPIO=kwargs.get('NOME_MUNICIPIO'),
                UF=kwargs.get('UF'),
                DIA=kwargs.get('DIA'),
                MES=kwargs.get('MES'),
            )
        return self


if __name__ == '__main__':  # pragma: no cover
    ic(
        municipios[0],
        type(municipios[0]),
        municipios[0]['UF'],
        municipios[0].get('UF'),
        '',
        # **municipios[0],
    )
    msm = MunicipioAPI(db, orm)
    ic(msm)
    msm.add(**municipios[0])
