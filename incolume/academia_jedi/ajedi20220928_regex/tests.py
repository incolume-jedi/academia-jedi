# !/usr/bin/env python
# -*- coding: utf-8 -*-
import incolume.academia_jedi.ajedi20220928_regex.app as app
import pytest
from faker import Faker

__author__ = "@britodfbr"  # pragma: no cover

fake = Faker('pt_BR')
fake.seed_instance(4321)


@pytest.fixture(scope='session', autouse=True)
def faker_session_locale():
    return ['pt_BR']


@pytest.fixture(scope='session', autouse=True)
def faker_seed():
    return 4321


@pytest.mark.parametrize(
    'entrance expected'.split(),
    zip(names := [fake.name() for _ in range(10)], names)   # Operador morsa
)
def test_example1(entrance, expected):
    assert app.example1(entrada=entrance) == expected


@pytest.mark.parametrize(
    'entrance',
    [fake.bothify(text='7#.###-###') for _ in range(10)]
    +[fake.bothify(text='8#.###-###') for _ in range(10)]
)
def test_example2(entrance):
    assert app.example2(entrance)


@pytest.mark.parametrize(
    'entrance',
    # [fake.random_number(digits=8) for _ in range(5)]
    [fake.bothify(text='####-####') for _ in range(15)]
)
def test_example3(entrance):
    if entrance[0] not in '0 7 8 9'.split():
        assert app.example3(entrada=entrance)
    else:
        assert not app.example3(entrance)


@pytest.mark.parametrize(
    'entrance',
    [fake.bothify(text='9####-####') for _ in range(5)]
    + [fake.bothify(text='8####-####') for _ in range(5)]
    + [fake.bothify(text='7####-####') for _ in range(5)]
    + [fake.bothify(text='#####-####') for _ in range(10)]
)
def test_example4(entrance):
    if entrance[0] in [x for x in '789']:
        assert app.example4(entrance)
    else:
        assert not app.example4(entrance)


def test_example5(faker, faker_session_locale, faker_seed):
    assert app.example5(faker.email())
