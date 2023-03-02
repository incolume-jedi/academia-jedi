# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "@britodfbr"  # pragma: no cover

import re
from collections import namedtuple

User = namedtuple("User", "name zipcode fone celfone email pw")
u1 = User(
    "Ricardo Brito do Nascimento",
    "72.000-000",
    "3535-3535",
    "93535-3535",
    "jesus@example.com",
    "a1B@§",
)


def show():
    regex = r"^[A-Z]+$"
    pattern = re.compile(regex, flags=re.I)
    print(
        pattern.search("HELLO"),
        pattern.search("HELLO WORLD"),
        pattern.search("Hello World"),
        pattern.search("hello world"),
        pattern.search("helloworld"),
        pattern.match("helloworld"),
        pattern.match("hello world"),
        pattern.fullmatch("hello world"),
        sep="\n",
    )


def example1(entrada: str) -> str:
    """
    Validação nome completo.
    """
    pat = re.compile(r"^(\w+\s)+\w+$", flags=re.I)
    result = pat.search(entrada)
    return pat.search(entrada).string if result else ""


def example2(entrada: str):
    """Validação CEP brasileiro."""
    pat = re.compile(r"^[78]\d\.?\d{3}-\d{3}$")
    return pat.match(entrada)


def example3(entrada: str):
    """Validação de telefone fixo."""
    pat = re.compile(r"^[1-6]\d{3}-?\d{4}$")
    return pat.match(entrada)


def example4(entrada: str):
    """Validação de telefone celular."""
    pat = re.compile(r"^[7-9]\d{4}-?\d{4}$")
    return pat.match(entrada)


def example5(entrada: str):
    """Validação de email."""
    pat = re.compile(
        r"^([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+$"
    )
    return pat.match(entrada)


def run():
    show()
    print("-" * 20)
    print(
        example1(u1.name),
        example2(u1.zipcode),
        example3(u1.fone),
        example4(u1.celfone),
        example5(u1.email),
        sep="\n",
    )


if __name__ == "__main__":  # pragma: no cover
    run()
