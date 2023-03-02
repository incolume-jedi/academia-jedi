# !/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List
from pprint import pprint
from faker import Faker
import datetime as dt
from models import pessoa
from deprecated import deprecated

__author__ = "@britodfbr"  # pragma: no cover

Faker.seed(13)
fake = Faker("pt_BR")


@deprecated(
    version="0.88.0",
    reason="Use an other implementation into 'incolume.academia_jedi.ajedi20220925"
    "_massa_dados_fake_protocol.generator_pessoas'",
)
def massa_pessoas(quantidade: int = 0) -> List:
    quantidade = quantidade or 100
    pessoas = [
        pessoa(
            nome_completo=(
                f"{fake.first_name()} {fake.last_name()} {fake.last_name()}"
            ),
            data_de_nascimento=fake.date_between(
                end_date=dt.datetime.strptime("2003-12-31", "%Y-%m-%d")
            ),
            cpf=fake.bothify(text="###.###.###-##"),
        )
        for _ in range(quantidade)
    ]

    return pessoas


def run():
    pprint(massa_pessoas(3))


if __name__ == "__main__":  # pragma: no cover
    run()
