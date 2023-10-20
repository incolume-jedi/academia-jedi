import logging

from textblob import Blobber, TextBlob

__author__ = '@britodfbr'  # pragma: no cover


def exemplo0():
    """"""
    frase = TextBlob('I havv goood speling!')
    print(frase.correct())


def exemplo1():
    """"""

    def corrigir_texto(texto):
        blob = TextBlob(texto)
        corrigido = blob.correct()
        return str(corrigido)

    texto = 'Este texto contém erros de ortografia e gramática. O aple é uma fruta.'
    texto_corrigido = corrigir_texto(texto)
    print(texto_corrigido)


def exemplo2():
    """"""

    def corrigir_texto(texto):
        blob = TextBlob(texto, language='pt-br')
        corrigido = blob.correct()
        return str(corrigido)

    texto = (
        'Este texto contém erros de ortografia. A camisa azul é mai bonita.'
    )
    texto_corrigido = corrigir_texto(texto)
    print(texto_corrigido)


def exemplo3():
    """"""

    def corrigir_texto(texto):
        blobber = Blobber(lang='pt')
        blob = blobber(texto)
        corrigido = blob.correct()
        return str(corrigido)

    texto = (
        'Este texto contém erros de ortografia. A camisa azul é mai bonita.'
    )
    texto_corrigido = corrigir_texto(texto)
    print(texto_corrigido)


def _exemplo4():
    """"""
    import nltk
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.naive_bayes import MultinomialNB
    from textblob import TextBlob
    from textblob.sentiments import NaiveBayesAnalyzer

    # Treinando o modelo com o corpus
    corpus = nltk.corpus.mac_morpho.tagged_sents()
    sentences = []
    tags = []
    for sent in corpus:
        sentence = ''
        tag = ''
        for word, tag_ in sent:
            sentence += word + ' '
            tag += tag_ + ' '
        sentences.append(sentence.strip())
        tags.append(tag.strip())

    vectorizer = CountVectorizer(lowercase=False)
    X = vectorizer.fit_transform(sentences)
    y = tags

    clf = MultinomialNB()
    clf.fit(X, y)

    # Corrigindo o texto com o modelo treinado
    def corrigir_texto(texto):
        blob = TextBlob(
            texto, pos_tagger=clf.predict_proba, analyzer=NaiveBayesAnalyzer()
        )
        corrigido = blob.correct()
        return str(corrigido)

    texto = (
        'Este texto contém erros de ortografia. A camisa azul é mai bonita.'
    )
    texto_corrigido = corrigir_texto(texto)
    print(texto_corrigido)


def exemplo5():
    """"""
    from nltk.corpus import brown
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.naive_bayes import MultinomialNB
    from textblob import TextBlob

    # Treinando o modelo com o corpus Brown
    corpus = brown.sents()
    corrected_corpus = []
    for sentence in corpus:
        text = ' '.join(sentence)
        corrected_text = TextBlob(text).correct()
        corrected_sentence = ' '.join(corrected_text.words)
        corrected_corpus.append(corrected_sentence)

    vectorizer = CountVectorizer(ngram_range=(1, 3))
    X = vectorizer.fit_transform(corrected_corpus)
    y = corpus

    clf = MultinomialNB()
    clf.fit(X, y)

    # Corrigindo o texto com o modelo treinado
    def correct_text(text):
        corrected_text = TextBlob(text).correct()
        corrected_words = corrected_text.words
        corrected_sentence = ' '.join(corrected_words)
        X_test = vectorizer.transform([corrected_sentence])
        y_pred = clf.predict(X_test)
        return ' '.join(y_pred[0])

    text = 'Ola, tudo ben?'
    corrected_text = correct_text(text)
    print(corrected_text)  # saída: "Ola , tudo bem ?"


def exemplo6():
    """"""
    from nltk.corpus import machado
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.naive_bayes import MultinomialNB
    from textblob import TextBlob

    # Treinando o modelo com o corpus Machado
    corpus = machado.sents()
    corrected_corpus = []
    for sentence in corpus:
        text = ' '.join(sentence)
        corrected_text = TextBlob(text).correct()
        corrected_sentence = ' '.join(corrected_text.words)
        corrected_corpus.append(corrected_sentence)

    vectorizer = CountVectorizer(ngram_range=(1, 3))
    X = vectorizer.fit_transform(corrected_corpus)
    y = corpus

    clf = MultinomialNB()
    clf.fit(X, y)

    # Corrigindo o texto com o modelo treinado
    def correct_text(text):
        corrected_text = TextBlob(text).correct()
        corrected_words = corrected_text.words
        corrected_sentence = ' '.join(corrected_words)
        X_test = vectorizer.transform([corrected_sentence])
        y_pred = clf.predict(X_test)
        return ' '.join(y_pred[0])

    text = 'Eu tenho um livvro muito interesssante para ler.'
    corrected_text = correct_text(text)
    print(
        corrected_text
    )  # saída: "Eu tenho um livro muito interessante para ler."


def _exemplo0():
    """"""

    # Exemplo de dados de treinamento


def run():
    functions = (b for a, b in globals().items() if a.startswith('exemplo'))
    for func in functions:
        logging.info(f'starting {func.__name__}')
        print('----')
        print(func.__name__)
        print('----')
        try:
            func()
        except (ValueError, AttributeError, TypeError) as e:
            logging.error(f'"{e.__class__.__name__}: {e}"')
        print()
        logging.info(f'finishing {func.__name__}')


if __name__ == '__main__':  # pragma: no cover
    run()
