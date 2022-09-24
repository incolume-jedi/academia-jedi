# !/usr/bin/env python
# -*- coding: utf-8 -*-
from app import run
from os import environ, getenv, putenv
from pprint import pprint


__author__ = "@britodfbr"  # pragma: no cover


def activate_envvar(activate: bool = False) -> bool:
    """Configura variavle de ambiente através do python."""
    # pprint(environ)
    if activate:
        environ['INCOLUME_AUTHOR'] = 'Ricardo Brito do Nascimento'
    return activate


activate_envvar(True)
run()
#  export INCOLUME_APPLICATION=MyApp; python main.py; unset INCOLUME_APPLICATION
