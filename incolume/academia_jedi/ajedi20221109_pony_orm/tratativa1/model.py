"""Model module."""

from pony import orm

__author__ = '@britodfbr'  # pragma: no cover

db = orm.Database()


def get_model_municipios(db, orm):
    """Get model."""

    class Municipios(db.Entity):
        __table__ = 'municipios'
        CODIGO_MUNICIPIO = orm.Required(str, unique=True)
        NOME_MUNICIPIO = orm.Required(str)
        UF = orm.Required(str)
        DIA = orm.Required(int)
        MES = orm.Required(int)

    return Municipios
