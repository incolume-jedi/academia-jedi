# !/usr/bin/env python
# -*- coding: utf-8 -*-
from dotenv import load_dotenv
from os import environ, getenv
from pprint import pprint


__author__ = "@britodfbr"  # pragma: no cover

load_dotenv()

for env in environ.items():
    print(env)
print(getenv("DOMAIN"))
print(getenv("ADMIN_EMAIL"))
print(getenv("ROOT_URL"))
