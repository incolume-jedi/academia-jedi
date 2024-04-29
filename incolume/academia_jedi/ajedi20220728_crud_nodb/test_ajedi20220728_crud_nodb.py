import pytest
from faker import Faker

from incolume.academia_jedi.ajedi20220728_crud_nodb.basedados import (
    create_person,
    db,
    delete_person,
    select_all_person,
    select_person,
    update_person,
)
from incolume.academia_jedi.ajedi20220728_crud_nodb.model import (
    Pessoa,
    gen_id,
    get_id,
)

Faker.seed(17)
fake = Faker('pt_Br')


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (0, 1),
        (10, 10),
        (100, 100),
    ],
)
def test_gen_id(entrance, expected):
    """Test gen id."""
    obj = gen_id(entrance)
    assert next(obj) == expected


@pytest.mark.parametrize(
    'expected',
    [
        1,
        2,
        3,
        4,
        5,
    ],
)
def test_get_id(expected: int) -> None:
    """Test get id"""
    assert get_id() == expected


@pytest.fixture()
def pessoa():
    """Fixture pessoa."""
    fname = fake.first_name()
    lname = fake.last_name()
    return Pessoa(
        f'{fname} {lname}',
        fake.date_time_this_century(),
        [f'{fname.casefold()}_{lname.casefold()}@example.org'],
    )


def test_create(pessoa):
    """Test create pessoa."""
    create_person(pessoa)
    assert db.get(pessoa.id) == pessoa
    db.clear()


def test_update(pessoa):
    """Test update pessoa."""
    create_person(pessoa)
    telefone = ['555-5555']
    pessoa.telefone = telefone
    update_person(pessoa.id, pessoa)
    assert db.get(pessoa.id).telefone == telefone
    db.clear()


def test_delete(pessoa):
    """Test delete pessoa."""
    create_person(pessoa)
    delete_person(pessoa.id)
    assert db.get(pessoa.id) is None
    db.clear()


def test_select(pessoa):
    """Test select pessoa."""
    create_person(pessoa)
    assert select_person(pessoa.id) == pessoa
    db.clear()


def test_select_all(pessoa):
    """Test select all."""
    create_person(pessoa)
    assert select_all_person() == [pessoa]
    db.clear()
