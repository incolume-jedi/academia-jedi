__author__ = '@britodfbr'  # pragma: no cover

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
import json
from dataclasses import dataclass
from pathlib import Path

from model import get_model_municipios
from pony import orm

db = orm.Database()

with (
    Path(__file__)
    .parents[4]
    .joinpath(
        'data_files',
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

    def add(self, *, kwargs):
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
    print(
        municipios[0],
        type(municipios[0]),
        municipios[0]['UF'],
        municipios[0].get('UF'),
        '',
        # **municipios[0],
    )
    msm = MunicipioAPI(db, orm)
    print(msm)
    msm.add(**municipios[0])
