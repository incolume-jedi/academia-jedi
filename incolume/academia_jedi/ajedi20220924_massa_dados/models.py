# !/usr/bin/env python

# ruff: noqa: D100, PYI024
from collections import namedtuple

__author__ = '@britodfbr'  # pragma: no cover

pessoa = namedtuple('Pessoa', ['nome_completo', 'data_de_nascimento', 'cpf'])
