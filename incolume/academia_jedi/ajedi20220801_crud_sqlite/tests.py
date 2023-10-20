import pytest
from basedados import (
    create_person,
    db,
)
from faker import Faker
from model import Pessoa

Faker.seed(17)
fake = Faker('pt_Br')


@pytest.fixture()
def pessoa():
    fname = fake.first_name()
    lname = fake.last_name()
    return Pessoa(
        f'{fname} {lname}',
        fake.date_time_this_century(),
        [f'{fname.casefold()}_{lname.casefold()}@example.org'],
    )


def test_create(pessoa):
    create_person(pessoa)
    assert db.get(pessoa.id) == pessoa
    db.clear()


def test_update(pessoa):
    create(pessoa)
    telefone = ['555-5555']
    pessoa.telefone = telefone
    update(pessoa.id, pessoa)
    assert db.get(pessoa.id).telefone == telefone
    db.clear()


def test_delete(pessoa):
    create(pessoa)
    delete(pessoa.id)
    assert db.get(pessoa.id) is None
    db.clear()


def test_select(pessoa):
    create(pessoa)
    assert select(pessoa.id) == pessoa
    db.clear()


def test_select_all(pessoa):
    create(pessoa)
    assert select_all() == [pessoa]
    db.clear()
