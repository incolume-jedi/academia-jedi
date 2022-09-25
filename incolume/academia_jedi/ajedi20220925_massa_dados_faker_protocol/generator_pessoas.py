# !/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List
from pprint import pprint
from faker import Faker
import datetime as dt
from models import Pessoa, Pessoa0, Event
from typing import Protocol


__author__ = "@britodfbr"  # pragma: no cover

Faker.seed(13)
fake = Faker('pt_BR')


class IPessoa(Protocol):
    """Definição do protocolo."""
    nome_completo: str
    data_de_nascimento: dt.datetime
    cpf: str


def massa_pessoas(
        objeto: IPessoa = None, quantidade: int = 0) -> List[IPessoa]:
    objeto = objeto or Pessoa
    quantidade = quantidade or 100
    return [
        objeto(
            nome_completo=(f'{fake.first_name()} '
                           f'{fake.last_name()} '
                           f'{fake.last_name()}'),
            data_de_nascimento=fake.date_between(
                start_date=dt.datetime.strptime('1970-01-01', '%Y-%m-%d'),
                end_date=dt.datetime.strptime('2003-12-31', '%Y-%m-%d')
            ),
            cpf=fake.bothify(text='###.###.###-##')
        )
        for _ in range(quantidade)
    ]


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
