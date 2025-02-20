# !/usr/bin/env python

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
import datetime as dt
import logging
from pprint import pprint
from typing import Protocol

from deprecated import deprecated
from faker import Faker

from incolume.academia_jedi.ajedi20220925_massa_dados_faker_protocol.models import (
    Event,
    Pessoa,
    Pessoa0,
)

__author__ = '@britodfbr'  # pragma: no cover

Faker.seed(13)
fake = Faker('pt_BR')


class IPessoa(Protocol):
    """Definição do protocolo."""

    nome_completo: str
    data_de_nascimento: dt.datetime
    cpf: str

    def jsonify(self): ...


@deprecated(
    version='0.88.0',
    reason="Use an other implementation into 'incolume.academia_"
    "jedi.ajedi20230211_massa_dados_fake_protocol.generator_pessoas'",
)
def massa_pessoas(
    objeto: IPessoa = None,
    quantidade: int = 0,
    is_json: bool = False,
) -> list[IPessoa]:
    logging.debug(f'params: {objeto=}, {quantidade=}, {is_json=}')
    objeto = objeto or Pessoa
    quantidade = quantidade or 100
    logging.debug(f'settings: {objeto=}, {quantidade=}, {is_json=}')
    result = [
        objeto(
            nome_completo=(
                f'{fake.first_name()} '
                f'{fake.last_name()} '
                f'{fake.last_name()}'
            ),
            data_de_nascimento=fake.date_between(
                start_date=dt.datetime.strptime('1965-01-01', '%Y-%m-%d'),
                end_date=dt.datetime.strptime('2003-12-31', '%Y-%m-%d'),
            ),
            cpf=fake.bothify(text='###.###.###-##'),
        )
        for _ in range(quantidade)
    ]
    return [pessoa.jsonify() for pessoa in result] if is_json else result


def run():
    print(massa_pessoas(objeto=Pessoa0, quantidade=5))
    print('\n---\n')

    try:
        # Validação de Protocolo
        print(massa_pessoas(objeto=Event, quantidade=3))
    except TypeError as e:
        print(e)

    print('\n---\n')
    pprint(massa_pessoas(objeto=Pessoa, quantidade=3))


if __name__ == '__main__':  # pragma: no cover
    run()
