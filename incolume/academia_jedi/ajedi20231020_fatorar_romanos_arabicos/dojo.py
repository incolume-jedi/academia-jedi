"""dojo 20231016."""
# !/usr/bin/env python
__author__ = '@britodfbr'  # pragma: no cover

romanos = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1,
}


def from_roman0(numero_romano: str) -> int:
    """Transforma número romanos em arábicos."""
    return romanos[numero_romano]


def from_roman(numero_romano: str) -> int:
    """Transforma número romanos em arábicos."""
    # MMIX
    result = 0
    qnt = len(numero_romano)
    for idx in range(qnt):
        if idx + 1 < qnt and (
            romanos[numero_romano[idx]] < romanos[numero_romano[idx + 1]]
        ):
            result -= romanos[numero_romano[idx]]
        else:
            result += romanos[numero_romano[idx]]

    return result
