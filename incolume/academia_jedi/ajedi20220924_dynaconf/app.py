# !/usr/bin/env python
# -*- coding: utf-8 -*-
from config import settings

__author__ = "@britodfbr"  # pragma: no cover
# MSG = "Hello World"   # changed to settings.toml do dynaconf


def run():
    """Chamadas de valores definidos pelo dynaconf."""
    print(
        settings.MSG,
        settings['MSG'],
        settings.msg,
        settings.get('msg'),
        settings.get('MSG'),
        f"Autor: {settings.get('author')}",
        f"App: {settings.get('application', 'examples_dynaconf')}",
        f"App: {settings.get('name', 'examples_dynaconf')}",
        f"{type(settings.get('FLOAT'))}: {settings.get('FLOAT')}",
        "{}: {}".format(settings.get('DICT'), type(settings.get('dict'))),
        "{}: {}".format(settings.get('BOOL'), type(settings.get('bool'))),
        "{}: {}".format(settings.get('DICT')['fuz'], type(settings.get('dict')['fuz'])),
        "{}: {}".format(settings.get('DICT').foo, type(settings.get('dict').foo)),
        "{}: {}".format(settings.get('NUM'), type(settings.get('num'))),
        "{}: {}".format(settings.get('NUMB'), type(settings.get('numb'))),
        "{}: {}".format(settings.get('NUMBER'), type(settings.get('number'))),
        settings.path,
        settings.data,
        settings.data.key,
        settings.data.newkey,
        sep='\n'
    )


if __name__ == '__main__':    # pragma: no cover
    run()
