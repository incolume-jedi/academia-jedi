# !/usr/bin/env python
"""Exemplos adaptados do site oficial.

https://docs.python.org/pt-br/dev/whatsnew/3.8.html
"""
import random
import re
from pathlib import Path
from unicodedata import normalize

from faker import Faker

__author__ = '@britodfbr'  # pragma: no cover

a = [random.randint(1, 10) for _ in range(random.randint(1, 30))]


def example1():
    if (n := len(a)) > 10:
        print(f'List is too long ({n} elements, expected <= 10)')


def example2():
    discount = 0.0
    advertisement = f'{random.randint(10, 40)}% discount'
    if mo := re.search(r'(\d+)% discount', advertisement):
        discount = float(mo.group(1)) / 100.0
    print(discount)


def example3():
    files = Path(__file__).parents[3].joinpath('data_files').glob('*.csv')
    file = random.choice(list(files))
    print(file)

    def process(value):
        """Fake process."""
        print('---\n', value, '\n---')

    with file.open() as f:
        # Loop over fixed length blocks
        while (block := f.read(256)) != '':
            process(block)


def example4(encode=False):
    """allowed_named not contains kwy."""
    fake = Faker('pt_Br' if encode else None)
    fake.seed_instance(13)
    names = [
        f'{fake.first_name()} {fake.last_name()} {fake.last_name()}'
        for _ in range(100)
    ]

    def allowed_names(name: str):
        return not bool(re.search('[kwy]', name, re.I))

    result = [
        clean_name.title()
        for name in names
        if (clean_name := normalize('NFC', name)) and allowed_names(clean_name)
    ]
    print(len(result), result)


def run():
    print(a)
    example1()
    example2()
    example3()
    example4()
    example4(True)
    ...


if __name__ == '__main__':
    run()
