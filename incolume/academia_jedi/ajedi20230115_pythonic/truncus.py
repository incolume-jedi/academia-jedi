from typing import List

import logging
from faker import Faker

Faker.seed(13)
fake = Faker("pt_BR")


def brazilian_name_list(length: int = 1) -> List[str]:
    logging.debug("Lista de nomes gerados.")
    return [f"{fake.first_name()} {fake.last_name()}" for _ in range(length)]
