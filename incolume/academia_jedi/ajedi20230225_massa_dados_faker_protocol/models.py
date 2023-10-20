"""Atualização de incolume.academia_jedi.ajedi20220925_massa_dados_faker_protocol.models."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime as dt
import json
import logging
import re
from copy import copy
from dataclasses import dataclass, field
from itertools import count

__author__ = '@britodfbr'  # pragma: no cover

import pytz

counter = count()


def date_parser(timestamp: str) -> dt.datetime:
    """"""
    regexes = {
        '%Y-%m-%dT%H:%M:%S.%f%z': re.compile(
            r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3,6}-\d{2}:\d{2}',
        ),
        '%Y-%m-%dT%H:%M:%S.%f': re.compile(
            r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3,6}',
        ),
        '%Y-%m-%dT%H:%M:%S%z': re.compile(
            r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{2}:\d{2}',
        ),
        '%Y-%m-%dT%H:%M:%S': re.compile(
            r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}',
        ),
        '%Y-%m-%d': re.compile(r'\d{4}-\d{2}-\d{2}'),
    }
    for regex in regexes.items():
        case = regex[1].fullmatch(timestamp)
        if case:
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



if __name__ == '__main__':  # pragma: no cover
    run()
