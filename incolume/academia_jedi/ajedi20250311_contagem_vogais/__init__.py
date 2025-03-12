"""Subpackage."""

import httpx
from bs4 import BeautifulSoup
from icecream import ic

url: str = 'https://pt.wikipedia.org/wiki/Python'

content: str = """
Python é uma linguagem de programação de alto nível,[10] interpretada de
 script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e
 forte. Foi lançada por Guido van Rossum em 1991.[1] Atualmente, possui um
 modelo de
 desenvolvimento comunitário, aberto e gerenciado pela organização sem fins
 lucrativos Python Software Foundation. Apesar de várias partes da linguagem
 possuírem padrões e especificações formais, a linguagem, como um todo, não é
 formalmente especificada. O padrão na pratica é a implementação CPython.

A linguagem foi projetada com a filosofia de enfatizar a importância do esforço
 do programador sobre o esforço computacional. Prioriza a legibilidade do
 código sobre a velocidade ou expressividade. Combina uma sintaxe concisa e
 clara com os recursos poderosos de sua biblioteca padrão e por módulos e
 frameworks desenvolvidos por terceiros.

Python é uma linguagem de propósito geral de alto nível, multiparadigma,
 suporta o paradigma orientado a objetos, imperativo, funcional e procedural.
 Possui tipagem dinâmica e uma de suas principais características é permitir
 a fácil leitura do código e exigir poucas linhas de código se comparado ao
 mesmo programa em outras linguagens. Devido às suas características, ela é
 utilizada, principalmente, para processamento de textos, dados científicos e
 criação de CGIs para páginas dinâmicas para a web. Foi considerada pelo
 público a 3ª linguagem "mais amada", de acordo com uma pesquisa conduzida
 pelo site Stack Overflow em 2018[11] e está entre as 5 linguagens mais
 populares, de acordo com uma pesquisa conduzida pela RedMonk.[12]

O nome Python teve a sua origem no grupo humorístico britânico Monty Python,
[13] criador do programa Monty Python's Flying Circus, embora muitas pessoas
 façam associação com o réptil do mesmo nome (em português, píton ou pitão).
"""


def get_text():
    """Get text."""
    resp = httpx.get(url)
    ic(resp)
    soup = BeautifulSoup(resp.content, 'html5lib')
    ic(soup)
    return soup.text


def count_vowels(text: str = '') -> dict:
    """Count vowels."""
    result = {}
    for vogal in 'aeiou':
        result[vogal] = text.casefold().count(vogal)
    return result
