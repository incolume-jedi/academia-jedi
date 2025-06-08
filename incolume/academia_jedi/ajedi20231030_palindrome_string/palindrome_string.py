"""Acaedmia 20231030."""

from __future__ import annotations

from unidecode import unidecode

# ruff: noqa: SIM103


def is_palindrome(valor: str | int) -> bool:
    """Verificar se o valor é um palíndromo."""
    valor = (
        unidecode(str(valor))
        .upper()
        .replace(' ', '')
        .replace(',', '')
        .replace('-', '')
    )
    if valor == valor[::-1]:
        return True
    return False
