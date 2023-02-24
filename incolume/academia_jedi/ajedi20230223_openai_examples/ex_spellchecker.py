import logging
import re
from spellchecker import SpellChecker
from nltk.tokenize import word_tokenize


def exemplo1():
    # Carrega o corretor ortográfico
    spell = SpellChecker()

    # Define o texto para correção
    texto = "Esse sit é muito legau"

    # Separa as palavras do texto
    palavras = texto.split()

    # Corrige a ortografia de cada palavra
    for palavra in palavras:
        # Verifica se a palavra está escrita corretamente
        if not spell.correction(palavra) == palavra:
            # Corrige a palavra
            correcao = spell.correction(palavra)
            # Substitui a palavra corrigida no texto
            texto = texto.replace(palavra, correcao)

    # Imprime o texto corrigido
    print(texto)


def exemplo2():
    # Carrega o corretor ortográfico em pt-BR
    spell = SpellChecker(language='pt')

    # Define o texto para correção
    texto = "Esse sit é muito legau"

    # Separa as palavras do texto
    palavras = texto.split()

    # Corrige a ortografia de cada palavra
    for palavra in palavras:
        # Verifica se a palavra está escrita corretamente
        if not spell.correction(palavra) == palavra:
            # Corrige a palavra
            correcao = spell.correction(palavra)
            # Substitui a palavra corrigida no texto
            texto = texto.replace(palavra, correcao)

    # Imprime o texto corrigido
    print(texto)


def exemplo3():
    """
    Neste exemplo, estamos utilizando o PySpellChecker para corrigir a
    ortografia de um texto. O texto é primeiro tokenizado em palavras usando
    a biblioteca NLTK e, em seguida, cada palavra é
    verificada pelo PySpellChecker.
    """

    # Carrega o corretor ortográfico
    spell = SpellChecker()

    # Define o texto para correção
    texto = "Eu adro meu trabalho e as pessos com quem trabalho."

    # Separa as palavras do texto
    palavras = word_tokenize(texto.lower())

    # Corrige a ortografia de cada palavra
    for i, palavra in enumerate(palavras):
        # Verifica se a palavra está escrita corretamente
        if palavra not in spell:
            # Sugere correções para a palavra incorreta
            sugestoes = spell.candidates(palavra)
            # Se houver sugestões de correção, substitui a palavra pela sugestão mais provável
            if sugestoes:
                palavras[i] = list(sugestoes)[0]

    # Concatena as palavras corrigidas para formar o texto corrigido
    texto_corrigido = " ".join(palavras)

    # Imprime o texto corrigido
    print(texto_corrigido)


def exemplo4():
    """
    Neste exemplo, estamos utilizando o PySpellChecker para corrigir a
    ortografia de um texto. O texto é primeiro tokenizado em palavras usando
    a biblioteca NLTK e, em seguida, cada palavra é
    verificada pelo PySpellChecker.
    """

    # Carrega o corretor ortográfico
    spell = SpellChecker()

    # Define o texto para correção
    texto = "Eu adro meu trabalho e as pessos com quem trabalho."

    # Separa as palavras do texto
    palavras = word_tokenize(texto.lower())

    # Corrige a ortografia de cada palavra
    for i, palavra in enumerate(palavras):
        # Verifica se a palavra está escrita corretamente
        if palavra not in spell:
            # Sugere correções para a palavra incorreta
            sugestoes = spell.candidates(palavra)
            # Se houver sugestões de correção, substitui a palavra pela sugestão mais provável
            if sugestoes:
                palavras[i] = list(sugestoes)[0]

    # Concatena as palavras corrigidas para formar o texto corrigido
    texto_corrigido = " ".join(palavras)

    # Imprime o texto corrigido
    print(texto_corrigido)


def exemplo5():
    """
    Neste exemplo, estamos utilizando o PySpellChecker em pt-br para corrigir a
    ortografia de um texto. O texto é primeiro tokenizado em palavras usando
    a biblioteca NLTK e, em seguida, cada palavra é
    verificada pelo PySpellChecker.
    """

    # Carrega o corretor ortográfico
    spell = SpellChecker(language="pt")

    # Define o texto para correção
    texto = "Eu adro meu trabalho e as pessos com quem trabalho."

    # Separa as palavras do texto
    palavras = word_tokenize(texto.lower())

    # Corrige a ortografia de cada palavra
    for i, palavra in enumerate(palavras):
        # Verifica se a palavra está escrita corretamente
        if palavra not in spell:
            # Sugere correções para a palavra incorreta
            sugestoes = spell.candidates(palavra)
            # Se houver sugestões de correção, substitui a palavra pela sugestão mais provável
            if sugestoes:
                palavras[i] = list(sugestoes)[0]

    # Concatena as palavras corrigidas para formar o texto corrigido
    texto_corrigido = " ".join(palavras)

    # Imprime o texto corrigido
    print(texto_corrigido)


def exemplo6():
    # Cria uma instância do corretor ortográfico para o idioma pt-br
    spell = SpellChecker(language='pt')

    # Corrige a ortografia de uma palavra
    palavra = 'carrtero'
    correcao = spell.correction(palavra)

    # Imprime a correção
    print(correcao)  # 'carteiro'


def exemplo7():
    """"""
    spell = SpellChecker(language='pt')

    def corrigir_texto(texto):
        palavras = texto.split()
        palavras_corrigidas = []
        for palavra in palavras:
            palavra_str = str(palavra)  # converte para string
            palavra_corrigida = spell.correction(palavra_str)
            palavras_corrigidas.append(palavra_corrigida)
        texto_corrigido = ' '.join(palavras_corrigidas)
        return texto_corrigido

    texto = 'Este texto está com varios eroos de ortografia'
    texto_corrigido = corrigir_texto(texto)
    print(texto_corrigido)


def run():
    # functions = (
    #     exemplo1,
    #     exemplo2,
    #
    # )
    # print(f for f in dict(globals().items()) if f.startswith('exemplo'))
    functions = (b for a, b in globals().items() if a.startswith('exemplo'))
    for func in functions:
        logging.info(f'starting {func.__name__}')
        print('----')
        print(func.__name__)
        print('----')
        func()
        print()
        logging.info(f'finishing {func.__name__}')


if __name__ == '__main__':    # pragma: no cover
    run()
