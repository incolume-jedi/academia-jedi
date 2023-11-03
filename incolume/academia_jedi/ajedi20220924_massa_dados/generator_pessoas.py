# !/usr/bin/env python
import datetime as dt
from pprint import pprint

from deprecated import deprecated
from faker import Faker
from .models import pessoa

__author__ = '@britodfbr'  # pragma: no cover

Faker.seed(13)
fake = Faker('pt_BR')


@deprecated(
    version='0.88.0',
    reason="Use an other implementation into 'incolume.academia_jedi.ajedi20220925"
    "_massa_dados_fake_protocol.generator_pessoas'",
)
def massa_pessoas(quantidade: int = 0) -> list:
    quantidade = quantidade or 100
    return [
        pessoa(
            nome_completo=(
                f'{fake.first_name()} {fake.last_name()} {fake.last_name()}'
            ),
            data_de_nascimento=fake.date_between(
                end_date=dt.datetime.strptime('2003-12-31', '%Y-%m-%d'),
            ),
            cpf=fake.bothify(text='###.###.###-##'),
        )
        for _ in range(quantidade)
    ]


def run():
    pprint(massa_pessoas(3))


if __name__ == '__main__':  # pragma: no cover
    run()
