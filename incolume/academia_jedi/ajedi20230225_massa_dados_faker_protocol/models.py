"""Atualização de incolume.academia_jedi.ajedi20220925_massa_dados_faker_protocol.models."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime as dt
import logging
from copy import copy
from dataclasses import dataclass, field, asdict
from itertools import count
import json
import re

__author__ = '@britodfbr'  # pragma: no cover

import pytz

counter = count()


def date_parser(timestamp: str) -> dt.datetime:
    """"""
    regexes = {
        '%Y-%m-%dT%H:%M:%S.%f%z': re.compile(
            r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3,6}-\d{2}:\d{2}'
        ),
        '%Y-%m-%dT%H:%M:%S.%f': re.compile(
            r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3,6}'
        ),
        '%Y-%m-%dT%H:%M:%S%z': re.compile(
            r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{2}:\d{2}'
        ),
        '%Y-%m-%dT%H:%M:%S': re.compile(
            r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}'
        ),
        '%Y-%m-%d': re.compile(r'\d{4}-\d{2}-\d{2}'),
    }
    for regex in regexes.items():
        case = regex[1].fullmatch(timestamp)
        if case:
            # print(case)
            print(dt.datetime.strptime(timestamp, regex[0]))


@dataclass
class Pessoa:
    nome_completo: str
    data_de_nascimento: dt.datetime
    cpf: str
    tz: str = field(default='America/Sao_Paulo', init=False)

    def __post_init__(self):
        if isinstance(self.data_de_nascimento, str):
            self.data_de_nascimento = date_parser(self.data_de_nascimento)

    def jsonify(self):
        temp = copy(self)
        try:
            temp.data_de_nascimento = (
                pytz.timezone(self.tz)
                .localize(self.data_de_nascimento)
                .isoformat()
            )
        except AttributeError as e:
            logging.error(e)
        return json.dumps(temp.__dict__)

    def to_dict(self):
        temp = copy(self)
        temp.data_de_nascimento = (
            pytz.timezone(self.tz)
            .localize(self.data_de_nascimento)
            .isoformat()
        )
        return temp.__dict__


def run():
    (date_parser('2023-02-13T19:52:24.891454546-03:00'))
    (date_parser('2023-02-13T19:52:24.8914545-03:00'))
    (date_parser('2023-02-13T19:52:24.891454-03:00'))
    (date_parser('2023-02-13T19:52:24.891454'))
    (date_parser('2023-02-13T19:52:24.454'))
    (date_parser('2023-02-13T19:52:24.891-03:00'))
    (date_parser('2023-02-13T19:52:24-03:00'))
    (date_parser('2023-02-13T19:52:24'))
    (date_parser('2011-11-11'))
    # print(date_parser('2023-02-13T19:52:24,891454546-03:00'))

    # p = Pessoa('João Filho', dt.datetime.now(), '123.456.789-01')
    # q = Pessoa('João Neto', '2011-11-11', '012.345.678-90')
    # r = Pessoa('João Junior', '2021-11-11', '012.345.678-90')
    # print(p, p.to_dict(), p.jsonify())
    # print(q, q.to_dict(), q.jsonify())
    # print(r, r.to_dict(), r.jsonify())


if __name__ == '__main__':  # pragma: no cover
    run()
