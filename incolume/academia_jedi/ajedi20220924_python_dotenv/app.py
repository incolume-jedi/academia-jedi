# !/usr/bin/env python

# ruff: noqa: D100
from os import environ, getenv

from dotenv import load_dotenv
from icecream import ic

__author__ = '@britodfbr'  # pragma: no cover

load_dotenv()

for env in environ.items():
    ic(env)
ic(getenv('DOMAIN'))
ic(getenv('ADMIN_EMAIL'))
ic(getenv('ROOT_URL'))
