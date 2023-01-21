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
        environ["INCOLUME_AUTHOR"] = "Ricardo Brito do Nascimento"
        environ["INCOLUME_NAME"] = "MyApp"
        environ["INCOLUME_NUM"] = "42"
        environ["INCOLUME_FLOAT"] = "4.2"
        environ["INCOLUME_BOOL"] = "true"
        environ["INCOLUME_DICT"] = '{foo="bar", fuz="foo"}'
        environ["INCOLUME_NUMBER"] = "@float 42"
        environ["INCOLUME_NUMB"] = "@str 42"
        environ["INCOLUME_PATH"] = "@format /tmp/xpto/{this.NAME}"
        environ["INCOLUME_DATA"] = '@json {"key": "value"}'
        environ["INCOLUME_DATA__newkey"] = "new value"
    return activate


activate_envvar(True)
run()

#  export INCOLUME_APPLICATION=MyApp; python main.py; unset INCOLUME_APPLICATION
"""
$ export INCOLUME_NUM=42
$ export INCOLUME_FLOAT=4.2
$ export INCOLUME_DICT='{foo="bar"}'
$ export INCOLUME_BOOL=false
$ export INCOLUME_NAME=MyApp
$ dynaconf --instance config.settings list
    Working in main environment
    MSG<str> 'Hello World'
    NUM<int> 42
    NAME<str> 'MyApp'
    DICT<dict> {'foo': 'bar'}
    FLOAT<float> 4.2
    BOOL<bool> False
export INCOLUME_MODE='production'; dynaconf --instance config.settings list
export INCOLUME_MODE='testing'; dynaconf --instance config.settings list
export INCOLUME_MODE='development'; dynaconf --instance config.settings list

"""
