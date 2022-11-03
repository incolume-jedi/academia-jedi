# !/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from typing import List
from pprint import pprint
from faker import Faker
import datetime as dt
from incolume.academia_jedi.ajedi20220925_massa_dados_faker_protocol\
    .models import Pessoa, Pessoa0, Event
from typing import Protocol


__author__ = "@britodfbr"  # pragma: no cover

Faker.seed(13)
fake = Faker('pt_BR')


class IPessoa(Protocol):
    """Definição do protocolo."""
    nome_completo: str
    data_de_nascimento: dt.datetime
    cpf: str

    def jsonify(self): ...


def massa_pessoas(
        objeto: IPessoa = None,
        quantidade: int = 0,
        is_json: bool = False) -> List[IPessoa]:

    logging.debug(f"params: {objeto=}, {quantidade=}, {is_json=}")
    objeto = objeto or Pessoa
    quantidade = quantidade or 100
    logging.debug(f"settings: {objeto=}, {quantidade=}, {is_json=}")
    result = [
        objeto(
            nome_completo=(f'{fake.first_name()} '
                           f'{fake.last_name()} '
                           f'{fake.last_name()}'),
            data_de_nascimento=fake.date_between(
                start_date=dt.datetime.strptime('1965-01-01', '%Y-%m-%d'),
                end_date=dt.datetime.strptime('2003-12-31', '%Y-%m-%d')
            ),
            cpf=fake.bothify(text='###.###.###-##')
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
    pprint(
        massa_pessoas(objeto=Pessoa, quantidade=3)
    )


if __name__ == '__main__':  # pragma: no cover
    run()
