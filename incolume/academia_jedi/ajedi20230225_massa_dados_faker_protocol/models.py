"""Atualização de incolume.academia_jedi.ajedi20220925_massa_dados_faker_protocol.models."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

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
            logging.exception(e)
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
