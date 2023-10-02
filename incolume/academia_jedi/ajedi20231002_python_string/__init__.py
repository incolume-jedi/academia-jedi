def python_string0(string):
    """Retorna uma string ao contrário."""
    result = ''
    for letra in string:
        result = letra + result
    return result


def python_string(string):
    """Retorna uma string ao contrário.
    
    Implementação pythonica
    """
    return string[::-1]