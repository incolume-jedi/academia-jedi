"""Truncus module."""

from faker import Faker
from incolume.academia_jedi import logger

Faker.seed(13)
fake = Faker('pt_BR')


def brazilian_name_list(length: int = 1) -> list[str]:
    """Nomes brasileiros."""
    logger.debug('Lista de nomes gerados.')
    return [f'{fake.first_name()} {fake.last_name()}' for _ in range(length)]
