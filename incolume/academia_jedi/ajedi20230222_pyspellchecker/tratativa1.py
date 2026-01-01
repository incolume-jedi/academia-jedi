"""Estudos com pyspellchecker."""

import logging

# ruff: noqa: G004
from spellchecker import SpellChecker


def ex1():
    """Criar um objeto SpellChecker para o português do Brasil."""
    spell = SpellChecker(language='pt')
    logging.debug(spell)

    # texto com palavras com erros ortográficos
    texto = 'Eu fiz uma conpra pela internete e a empressa entrego errado.'
    logging.debug('texto=%s', texto)

    # separar o texto em palavras
    palavras = texto.split()
    logging.debug(f'{palavras}')

    # verificar a ortografia de cada palavra
    for palavra in palavras:
        s = spell.correction(palavra)
        logging.debug(f'{palavra}: {s=}')
        if s != palavra:
            print(
                f'A palavra {palavra} está'
                f' escrita incorretamente. Sugestão: {s}',
            )
