import logging

from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from spellchecker import SpellChecker


def exemplo1():
    # Carrega o corretor ortográfico
    spell = SpellChecker()

    # Define um conjunto de textos para treinamento
    textos_treinamento = [
        'Eu sempre gosto de correr no parque',
        'Eu gosto de laranjas, mas não de maçãs',
        'A música é minha paixão desde que eu era criança',
        'O cachorro late o dia todo no quintal',
        'A matemática é uma ciência fascinante',
    ]
    logging.debug(textos_treinamento)

    # Extrai as palavras dos textos de treinamento
    palavras_treinamento = [
        word_tokenize(texto.lower()) for texto in textos_treinamento
    ]
    logging.debug(palavras_treinamento)

    # Cria um vetor de características com as palavras únicas dos textos de treinamento
    vetorizador = CountVectorizer(tokenizer=lambda doc: doc, lowercase=False)
    logging.debug(vetorizador)
    vetor_caracteristicas = vetorizador.fit_transform(palavras_treinamento)
    logging.debug(vetor_caracteristicas)

    # Cria um modelo de classificação para prever se uma palavra está correta ou não
    modelo = LogisticRegression(max_iter=5000)
    logging.debug(modelo)

    y_treinamento = [
        1 if palavra in spell else 0
        for texto in palavras_treinamento
        for palavra in texto
    ]

    modelo.fit(vetor_caracteristicas, y_treinamento)

    # Define o texto para correção
    texto = 'Ela comprou uma blusa azul no shoping'
    logging.debug(texto)

    # Separa as palavras do texto
    palavras = word_tokenize(texto.lower())
    logging.debug(palavras)

    # Corrige a ortografia de cada palavra
    for i, palavra in enumerate(palavras):
        # Verifica se a palavra está escrita corretamente
        if palavra not in spell:
            # Extrai as características da palavra para alimentar o modelo de classificação
            x = vetorizador.transform([palavra])
            # Classifica a palavra como correta ou incorreta
            y = modelo.predict(x)[0]
            # Se a palavra for classificada como correta, mantém a palavra original
            if y == 1:
                palavras[i] = palavra
            # Caso contrário, substitui a palavra pela sugestão mais provável
            else:
                sugestoes = spell.candidates(palavra)
                palavras[i] = (
                    spell.correction(palavra)
                    if not sugestoes
                    else sugestoes[0]
                )

    # Concatena as palavras corrigidas para formar o texto corrigido
    texto_corrigido = ' '.join(palavras)
    logging.debug(f'{texto_corrigido=}')
    # Imprime o texto corrigido
    print(texto_corrigido)


def exemplo2():
    """"""

    from nltk.tokenize import word_tokenize
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.linear_model import LogisticRegression
    from spellchecker import SpellChecker

    # Carrega o corretor ortográfico
    spell = SpellChecker()

    # Define um conjunto de textos para treinamento
    textos_treinamento = [
        'Eu sempre gosto de correr no parque',
        'Eu gosto de laranjas, mas não de maçãs',
        'A música é minha paixão desde que eu era criança',
        'O cachorro late o dia todo no quintal',
        'A matemática é uma ciência fascinante',
    ]

    # Extrai as palavras dos textos de treinamento
    palavras_treinamento = [
        word_tokenize(texto.lower()) for texto in textos_treinamento
    ]

    # Cria um vetor de características com as palavras únicas dos textos de treinamento
    vetorizador = CountVectorizer(tokenizer=lambda doc: doc, lowercase=False)
    vetor_caracteristicas = vetorizador.fit_transform(
        [palavra for texto in palavras_treinamento for palavra in texto]
    )

    # Cria um modelo de classificação para prever se uma palavra está correta ou não
    modelo = LogisticRegression(max_iter=5000)
    y_treinamento = [
        1 if palavra in spell else 0
        for texto in palavras_treinamento
        for palavra in texto
    ]
    modelo.fit(vetor_caracteristicas, y_treinamento)

    # Define o texto para correção
    texto = 'Ela comprou uma blusa azul no shoping'

    # Separa as palavras do texto
    palavras = word_tokenize(texto.lower())

    # Corrige a ortografia de cada palavra
    for i, palavra in enumerate(palavras):
        # Verifica se a palavra está escrita corretamente
        if palavra not in spell:
            # Extrai as características da palavra para alimentar o modelo de classificação
            x = vetorizador.transform([palavra])
            # Classifica a palavra como correta ou incorreta
            y = modelo.predict(x)[0]
            # Se a palavra for classificada como correta, mantém a palavra original
            if y == 1:
                palavras[i] = palavra
            # Caso contrário, substitui a palavra pela sugestão mais provável
            else:
                sugestoes = spell.candidates(palavra)
                palavras[i] = (
                    spell.correction(palavra)
                    if not sugestoes
                    else list(sugestoes)[0]
                )

    # Concatena as palavras corrigidas para formar o texto corrigido
    texto_corrigido = ' '.join(palavras)

    # Imprime o texto corrigido
    print(texto_corrigido)


def exemplo3():
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.naive_bayes import MultinomialNB
    from spellchecker import SpellChecker

    # Cria uma instância do corretor ortográfico para o idioma pt-br
    spell = SpellChecker(language='pt')

    # Define os dados de treinamento e teste
    textos_treinamento = [
        'Este é um texto de exemplo',
        'O carrtero entregou a carta',
        'O aviaum decolou do aeroporto',
        'Vou almoçar no resauranti',
        'Amanhã irei ao medico',
    ]

    textos_teste = [
        'Este texto está com erros de ortografia',
        'O coretor ortográfico pode ajudar',
        'Vou ao restaruante hoje',
        'O avião está preste a decolar',
    ]

    # Prepara os dados de entrada
    cv = CountVectorizer(strip_accents='unicode', lowercase=True)
    X_treinamento = cv.fit_transform(textos_treinamento)
    cv.transform(textos_teste)

    # Treina o modelo de aprendizado de máquina
    y_treinamento = ['exemplo', 'carta', 'avião', 'restaurante', 'médico']
    modelo = MultinomialNB()
    modelo.fit(X_treinamento, y_treinamento)

    # Corrige a ortografia dos textos de teste
    textos_corrigidos = []
    for texto in textos_teste:
        palavras = texto.split()
        palavras_corrigidas = []
        for palavra in palavras:
            # Verifica se a palavra está correta
            if spell.correction(palavra) == palavra:
                palavras_corrigidas.append(palavra)
            else:
                # Se a palavra estiver incorreta, usa o modelo de ML para sugerir a correção
                palavras_sugeridas = cv.transform(
                    list(spell.candidates(palavra))
                )
                sugestao = modelo.predict(palavras_sugeridas)[0]
                palavras_corrigidas.append(sugestao)
        texto_corrigido = ' '.join(palavras_corrigidas)
        textos_corrigidos.append(texto_corrigido)

    # Imprime os textos corrigidos
    for texto in textos_corrigidos:
        print(texto)


def run():
    functions = (b for a, b in globals().items() if a.startswith('exemplo'))
    for func in functions:
        logging.info(f'starting {func.__name__}')
        print('----')
        print(func.__name__)
        print('----')
        try:
            func()
        except (ValueError) as e:
            logging.error(f'"{e.__class__.__name__}: {e}"')
        print()
        logging.info(f'finishing {func.__name__}')


if __name__ == '__main__':  # pragma: no cover
    run()
