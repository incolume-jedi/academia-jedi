"""Estudos com pyspellchecker."""

# ruff: noqa: G004
import logging

from icecream import ic
from spellchecker import SpellChecker


def ex0():
    """Exemplo da documentação em pypi."""
    spell = SpellChecker()

    # find those words that may be misspelled
    misspelled = spell.unknown(['something', 'is', 'hapenning', 'here'])

    for word in misspelled:
        # Get the one `most likely` answer
        ic(spell.correction(word))

        # Get a list of `likely` options
        ic(spell.candidates(word))


def ex1():
    """Criar um objeto SpellChecker para o português do Brasil."""
    spell = SpellChecker(language='pt')
    logging.debug(spell)

    # texto com palavras com erros ortográficos
    texto = 'Eu fiz uma conpra pela internete e a empressa entrego errado.'
    logging.debug('texto=%s', texto)

    # separar o texto em palavras
    palavras = texto.split()
    logging.debug(palavras)

    # verificar a ortografia de cada palavra
    for palavra in palavras:
        s = spell.correction(palavra)
        logging.debug(f'{palavra}: {s=}')
        if s != palavra:
            ic(
                f'A palavra {palavra} está'
                f' escrita incorretamente. Sugestão: {s}',
            )
