# !/usr/bin/env python

__author__ = '@britodfbr'  # pragma: no cover


def get_model_municipios(db, orm):
    class Municipios(db.Entity):
        __table__ = 'municipios'
        CODIGO_MUNICIPIO = orm.Required(str, unique=True)
        NOME_MUNICIPIO = orm.Required(str)
        UF = orm.Required(str)
        DIA = orm.Required(int)
        MES = orm.Required(int)

    return Municipios
