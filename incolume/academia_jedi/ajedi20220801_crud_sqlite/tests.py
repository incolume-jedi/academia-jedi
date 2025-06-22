import pytest
from faker import Faker
from incolume.academia_jedi.ajedi20220801_crud_sqlite.basedados import (
    create_person,
    db,
    delete_person,
    select_all_person,
    select_person,
    update_person,
)
from incolume.academia_jedi.ajedi20220801_crud_sqlite.model import Pessoa

# ruff: noqa: D100, D103, S101

Faker.seed(17)
fake = Faker('pt_Br')


@pytest.fixture
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
    create_person(pessoa)
    telefone = ['555-5555']
    pessoa.telefone = telefone
    update_person(pessoa.id, pessoa)
    assert db.get(pessoa.id).telefone == telefone
    db.clear()


def test_delete(pessoa):
    create_person(pessoa)
    delete_person(pessoa.id)
    assert db.get(pessoa.id) is None
    db.clear()


def test_select(pessoa):
    create_person(pessoa)
    assert select_person(pessoa.id) == pessoa
    db.clear()


def test_select_all(pessoa):
    create_person(pessoa)
    assert select_all_person() == [pessoa]
    db.clear()
