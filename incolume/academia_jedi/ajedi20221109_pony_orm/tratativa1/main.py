__author__ = "@britodfbr"  # pragma: no cover
import json
from dataclasses import dataclass
from pathlib import Path
from pony import orm
from model import get_model_municipios


db = orm.Database()

with Path(__file__).parents[4].joinpath("data_files", "municipios_br.json").open() as f:
    municipios = json.load(f)


@dataclass
class MunicipioAPI:
    def __init__(self, db, orm):
        self.db = db
        self.orm = orm

    def add(self, *, kwargs):
        with orm.db_session:
            new_municipio = get_model_municipios(self.db, self.orm)
            new_municipio(
                CODIGO_MUNICIPIO=kwargs.get("CODIGO_MUNICIPIO"),
                NOME_MUNICIPIO=kwargs.get("NOME_MUNICIPIO"),
                UF=kwargs.get("UF"),
                DIA=kwargs.get("DIA"),
                MES=kwargs.get("MES"),
            )
        return self


if __name__ == "__main__":  # pragma: no cover
    print(
        municipios[0],
        type(municipios[0]),
        municipios[0]["UF"],
        municipios[0].get("UF"),
        "",
        # **municipios[0],
    )
    msm = MunicipioAPI(db, orm)
    print(msm)
    msm.add(**municipios[0])
    # msm.add(**{'CODIGO_MUNICIPIO': 520005, 'NOME_MUNICIPIO': 'Abadia de Goiás', 'DIA': 29, 'MES': 3})
