"""Reverse string."""


def python_string0(string: str) -> str:
    """Retorna uma string ao contrário."""
    result = ''
    for letra in string:
        result = letra + result
    return result


def python_string(string: str) -> str:
    """Retorna uma string ao contrário.

    Implementação pythonica
    """
    return string[::-1]
