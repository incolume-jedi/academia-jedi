from spellchecker import SpellChecker
import logging


def ex1():
    # criar um objeto SpellChecker para o português do Brasil
    spell = SpellChecker(language='pt')
    logging.debug(spell)

    # texto com palavras com erros ortográficos
    texto = "Eu fiz uma conpra pela internete e a empressa entrego errado."
    logging.debug(f'{texto=}')

    # separar o texto em palavras
    palavras = texto.split()
    logging.debug(f'{palavras}')

    # verificar a ortografia de cada palavra
    for palavra in palavras:
        s = spell.correction(palavra)
        logging.debug(f'{palavra}: {s=}')
        if not s == palavra:
            print(f"A palavra {palavra} está"
                  f" escrita incorretamente. Sugestão: {s}")


