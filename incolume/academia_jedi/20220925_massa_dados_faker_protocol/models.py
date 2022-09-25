# !/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime as dt
from collections import namedtuple
from dataclasses import dataclass, field
from itertools import count


__author__ = "@britodfbr"  # pragma: no cover
counter = count()

Pessoa0 = namedtuple('Pessoa', ['nome_completo', 'data_de_nascimento', 'cpf'])


@dataclass
class Pessoa:
    nome_completo: str
    data_de_nascimento: dt.datetime
    cpf: str


@dataclass
class Event:
    message: str
    create_at: dt.datetime = field(default_factory=dt.datetime.now)
    index: int = field(default_factory=lambda: next(counter))
