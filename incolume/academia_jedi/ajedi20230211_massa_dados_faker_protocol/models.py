"""Atualização de incolume.academia_jedi.ajedi20220925_massa_dados_faker_protocol.models."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime as dt
from copy import copy
from dataclasses import dataclass, field
from itertools import count
import json

__author__ = "@britodfbr"  # pragma: no cover
counter = count()


@dataclass
class Pessoa:
    nome_completo: str
    data_de_nascimento: dt.datetime
    cpf: str

    def jsonify(self):
        temp = copy(self)
        temp.data_de_nascimento = self.data_de_nascimento.strftime("%Y-%m-%d")
        return json.dumps(temp.__dict__)

    def to_dict(self):
        return self.__dict__


if __name__ == '__main__':    # pragma: no cover
    p = Pessoa('João Filho', dt.datetime.now(), '123.456.789-01')
    print(p.to_dict())
    print(p.jsonify())
