import logging

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
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
            texto,
            pos_tagger=clf.predict_proba,
            analyzer=NaiveBayesAnalyzer(),
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
        corrected_text,
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
            logging.exception(f'"{e.__class__.__name__}: {e}"')
        print()
        logging.info(f'finishing {func.__name__}')


if __name__ == '__main__':  # pragma: no cover
    run()
