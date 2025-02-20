import logging

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
from nltk.tokenize import word_tokenize
from spellchecker import SpellChecker


def exemplo1():
    # Carrega o corretor ortográfico
    spell = SpellChecker()

    # Define o texto para correção
    texto = 'Esse sit é muito legau'

    # Separa as palavras do texto
    palavras = texto.split()

    # Corrige a ortografia de cada palavra
    for palavra in palavras:
        # Verifica se a palavra está escrita corretamente
        if spell.correction(palavra) != palavra:
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
    texto = 'Esse sit é muito legau'

    # Separa as palavras do texto
    palavras = texto.split()

    # Corrige a ortografia de cada palavra
    for palavra in palavras:
        # Verifica se a palavra está escrita corretamente
        if spell.correction(palavra) != palavra:
            # Corrige a palavra
            correcao = spell.correction(palavra)
            # Substitui a palavra corrigida no texto
            texto = texto.replace(palavra, correcao)

    # Imprime o texto corrigido
    print(texto)


def exemplo3():
    """Neste exemplo, estamos utilizando o PySpellChecker para corrigir a
    ortografia de um texto. O texto é primeiro tokenizado em palavras usando
    a biblioteca NLTK e, em seguida, cada palavra é
    verificada pelo PySpellChecker.
    """
    # Carrega o corretor ortográfico
    spell = SpellChecker()

    # Define o texto para correção
    texto = 'Eu adro meu trabalho e as pessos com quem trabalho.'

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
                palavras[i] = next(iter(sugestoes))

    # Concatena as palavras corrigidas para formar o texto corrigido
    texto_corrigido = ' '.join(palavras)

    # Imprime o texto corrigido
    print(texto_corrigido)


def exemplo4():
    """Neste exemplo, estamos utilizando o PySpellChecker para corrigir a
    ortografia de um texto. O texto é primeiro tokenizado em palavras usando
    a biblioteca NLTK e, em seguida, cada palavra é
    verificada pelo PySpellChecker.
    """
    # Carrega o corretor ortográfico
    spell = SpellChecker()

    # Define o texto para correção
    texto = 'Eu adro meu trabalho e as pessos com quem trabalho.'

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
                palavras[i] = next(iter(sugestoes))

    # Concatena as palavras corrigidas para formar o texto corrigido
    texto_corrigido = ' '.join(palavras)

    # Imprime o texto corrigido
    print(texto_corrigido)


def exemplo5():
    """Neste exemplo, estamos utilizando o PySpellChecker em pt-br para corrigir a
    ortografia de um texto. O texto é primeiro tokenizado em palavras usando
    a biblioteca NLTK e, em seguida, cada palavra é
    verificada pelo PySpellChecker.
    """
    # Carrega o corretor ortográfico
    spell = SpellChecker(language='pt')

    # Define o texto para correção
    texto = 'Eu adro meu trabalho e as pessos com quem trabalho.'

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
                palavras[i] = next(iter(sugestoes))

    # Concatena as palavras corrigidas para formar o texto corrigido
    texto_corrigido = ' '.join(palavras)

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
        return ' '.join(palavras_corrigidas)

    texto = 'Este texto está com varios eroos de ortografia'
    texto_corrigido = corrigir_texto(texto)
    print(texto_corrigido)


def run():
    #     exemplo1,
    #     exemplo2,
    #
    functions = (b for a, b in globals().items() if a.startswith('exemplo'))
    for func in functions:
        logging.info(f'starting {func.__name__}')
        print('----')
        print(func.__name__)
        print('----')
        func()
        print()
        logging.info(f'finishing {func.__name__}')


if __name__ == '__main__':  # pragma: no cover
    run()
