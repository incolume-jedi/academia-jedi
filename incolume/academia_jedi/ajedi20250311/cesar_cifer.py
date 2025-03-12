"""Cesar cifer module."""

import string


def rot13a(texto: str) -> str:
    """Rot13."""
    d = {}
    if not texto:
        return texto

    for c in (65, 97):
        for i in range(26):
            d[chr(i + c)] = chr((i + 13) % 26 + c)
    return ''.join([d.get(c, c) for c in texto])


def cesar_cifer(text: str = '', key: int = 0) -> str:
    """Cesar cifer."""
    result = ''
    length = len(string.ascii_lowercase)
    code = {
        chr(char + idx): chr((idx + key) % length + char)
        for char in (65, 97)
        for idx in range(length)
    }

    for letra in text:
        result += code.get(letra, letra)
    return result
