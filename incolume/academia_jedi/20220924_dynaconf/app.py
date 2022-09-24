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
        sep='\n'
    )


if __name__ == '__main__':    # pragma: no cover
    run()
