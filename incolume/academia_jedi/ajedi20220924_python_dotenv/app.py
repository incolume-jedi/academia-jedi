# !/usr/bin/env python

# ruff: noqa: D100
from os import environ, getenv

from dotenv import load_dotenv

__author__ = '@britodfbr'  # pragma: no cover

load_dotenv()

for env in environ.items():
    print(env)
print(getenv('DOMAIN'))
print(getenv('ADMIN_EMAIL'))
print(getenv('ROOT_URL'))
