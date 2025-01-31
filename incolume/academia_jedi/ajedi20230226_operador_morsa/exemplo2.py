"""Exemplos adaptados do site oficial."""

import re
import secrets
from pathlib import Path
from unicodedata import normalize

from faker import Faker
from icecream import ic

__author__ = '@britodfbr'  # pragma: no cover

a = [secrets.randbelow(30) for _ in range(secrets.randbelow(10))]


def example1(tries: int = 10) -> None:
    """Example1."""
    if (n := len(a)) > tries:
        ic(f'List is too long ({n} elements, expected <= 10)')


def example2():
    """Example2."""
    discount = 0.0
    advertisement = f'{secrets.randbelow(40)}% discount'
    if mo := re.search(r'(\d+)% discount', advertisement):
        discount = float(mo.group(1)) / 100.0
    ic(discount)


def example3():
    """Example3."""
    files = Path(__file__).parents[3].joinpath('data_files').glob('*.csv')
    file = secrets.choice(list(files))
    ic(file)

    def process(value):
        """Fake process."""
        ic(f'---\n{value}\n---')

    with file.open() as f:
        # Loop over fixed length blocks
        while (block := f.read(256)) != '':
            process(block)


def example4(*, encode: bool = False) -> None:
    """allowed_named not contains kwy."""
    fake = Faker('pt_Br' if encode else None)
    fake.seed_instance(13)
    names = [
        f'{fake.first_name()} {fake.last_name()} {fake.last_name()}'
        for _ in range(100)
    ]

    def allowed_names(name: str) -> bool:
        """Allowed names."""
        return not bool(re.search('[kwy]', name, re.I))

    result = [
        clean_name.title()
        for name in names
        if (clean_name := normalize('NFC', name)) and allowed_names(clean_name)
    ]
    ic(len(result), result)


def run():
    """Run it."""
    ic(a)
    example1()
    example2()
    example3()
    example4()
    example4(encode=True)


if __name__ == '__main__':
    run()
