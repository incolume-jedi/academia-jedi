# !/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime as dt
import logging
from pprint import pprint
from typing import List, Protocol

from faker import Faker

from incolume.academia_jedi.ajedi20230211_massa_dados_faker_protocol.models import (
    Pessoa,
)

__author__ = '@britodfbr'  # pragma: no cover

Faker.seed(13)
fake = Faker('pt_BR')


class IPessoa(Protocol):
    """Definição do protocolo."""

    nome_completo: str
    data_de_nascimento: dt.datetime
    cpf: str

    def jsonify(self):
        ...


def get_password(num: int):
    return fake.bothify(
        text=r'^(?=(?:.*[a-z]){2})(?=(?:.*[A-Z]){2})(?=(?:.*\d){2})(?=(?:.*[@$!%*?&]){2})[A-Za-z\d@$!%*?&]{8,}$'
    )


def massa_pessoas(
    objeto: IPessoa = None,
    quantidade: int = 10,
    type: str | None = None,
) -> List[IPessoa]:
    logging.debug(f'params: {objeto=}, {quantidade=}, {type=}')
    objeto = objeto or Pessoa
    quantidade: int = quantidade or 100
    logging.debug(f'settings: {objeto=}, {quantidade=}, {type=}')
    result = [
        objeto(
            nome_completo=(
                f'{fake.first_name()} '
                f'{fake.last_name()} '
                f'{fake.last_name()}'
            ),
            data_de_nascimento=(
                dt.datetime.combine(  # convert date > datetime
                    fake.date_between(  # Date fake
                        start_date=dt.datetime.strptime(
                            '1965-01-01', '%Y-%m-%d'
                        ),
                        end_date=dt.datetime.strptime(
                            '2003-12-31', '%Y-%m-%d'
                        ),
                    ),
                    dt.time(),  # time supplementary
                )
            ),
            cpf=fake.bothify(text='###.###.###-##'),
        )
        for _ in range(quantidade)
    ]
    match type:
        case 'json':
            return [pessoa.jsonify() for pessoa in result]
        case 'dict':
            return [pessoa.to_dict() for pessoa in result]
        case _:
            return result


def run():
    print('\n---\n')
    pprint(massa_pessoas(quantidade=2))
    pprint(massa_pessoas(quantidade=3, type='json'))
    pprint(massa_pessoas(quantidade=3, type='dict'))
    pprint(get_password(8))


if __name__ == '__main__':  # pragma: no cover
    run()
