# !/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime as dt
import json
from collections import namedtuple
from copy import copy
from dataclasses import dataclass, field
from itertools import count

__author__ = '@britodfbr'  # pragma: no cover
counter = count()

Pessoa0 = namedtuple('Pessoa', ['nome_completo', 'data_de_nascimento', 'cpf'])


@dataclass
class Pessoa:
    nome_completo: str
    data_de_nascimento: dt.datetime
    cpf: str

    def jsonify(self):
        temp = copy(self)
        temp.data_de_nascimento = self.data_de_nascimento.isoformat()
        return json.dumps(temp.__dict__)

    def to_dict(self):
        temp = copy(self)
        temp.data_de_nascimento = self.data_de_nascimento.isoformat()
        return temp.__dict__


@dataclass
class Event:
    message: str
    create_at: dt.datetime = field(default_factory=dt.datetime.now)
    index: int = field(default_factory=lambda: next(counter))
