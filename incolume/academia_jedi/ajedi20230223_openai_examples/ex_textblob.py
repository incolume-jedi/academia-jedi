from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from textblob import Blobber
from textblob.sentiments import NaiveBayesAnalyzer
import logging

__author__ = "@britodfbr"  # pragma: no cover


def exemplo0():
    """"""
    frase = TextBlob("I havv goood speling!")
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

    texto = 'Este texto contém erros de ortografia. A camisa azul é mai bonita.'
    texto_corrigido = corrigir_texto(texto)
    print(texto_corrigido)


def exemplo3():
    """"""

    def corrigir_texto(texto):
        blobber = Blobber(lang='pt')
        blob = blobber(texto)
        corrigido = blob.correct()
        return str(corrigido)

    texto = 'Este texto contém erros de ortografia. A camisa azul é mai bonita.'
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
        sentence = ""
        tag = ""
        for word, tag_ in sent:
            sentence += word + " "
            tag += tag_ + " "
        sentences.append(sentence.strip())
        tags.append(tag.strip())

    vectorizer = CountVectorizer(lowercase=False)
    X = vectorizer.fit_transform(sentences)
    y = tags

    clf = MultinomialNB()
    clf.fit(X, y)

    # Corrigindo o texto com o modelo treinado
    def corrigir_texto(texto):
        blob = TextBlob(texto, pos_tagger=clf.predict_proba,
                        analyzer=NaiveBayesAnalyzer())
        corrigido = blob.correct()
        return str(corrigido)

    texto = 'Este texto contém erros de ortografia. A camisa azul é mai bonita.'
    texto_corrigido = corrigir_texto(texto)
    print(texto_corrigido)


def exemplo5():
    """"""
    import nltk
    from textblob import TextBlob
    from nltk.corpus import brown
    from sklearn.naive_bayes import MultinomialNB
    from sklearn.feature_extraction.text import CountVectorizer

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

    text = "Ola, tudo ben?"
    corrected_text = correct_text(text)
    print(corrected_text)  # saída: "Ola , tudo bem ?"


def exemplo6():
    """"""
    import nltk
    from textblob import TextBlob
    from nltk.corpus import machado
    from sklearn.naive_bayes import MultinomialNB
    from sklearn.feature_extraction.text import CountVectorizer

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

    text = "Eu tenho um livvro muito interesssante para ler."
    corrected_text = correct_text(text)
    print(
        corrected_text)  # saída: "Eu tenho um livro muito interessante para ler."


def _exemplo0():
    """"""

    # Exemplo de dados de treinamento
    train = [
        ('Este carro é muito bom', 'correto'),
        ('Estou indo para a casa', 'correto'),
        ('Eu gosto de gatas', 'incorreto'),
        ('Este time é campeão', 'correto'),
        ('A bela adormecida é uma historia infantil', 'correto'),
        ('Ele fizeram o jantar', 'incorreto'),
        ('Ela vai pra igreja todo domingo', 'correto'),
        ('Eu presciso comprar leite', 'incorreto'),
        ('O céu é azul', 'correto'),
        ('Ela disse que ta com fome', 'correto'),
        ('Eles compraram duas camisas', 'correto'),
        ('Eu já fui no cinema com ela', 'correto'),
        ('Ouviram do Ipiranga as margens plácidas', 'correto'),
        ('Eu prefiro cerveja do que vinho', 'correto'),
        ('Ela mora perto do trabalho', 'correto'),
        ('Este filme é ótimo', 'correto'),
        ('Eles gostam de dançar samba', 'correto'),
        ('Este livro é interessante', 'correto'),
        ('Eu tenho um gato em casa', 'correto'),
        ('Eu tomo café todas as manhãs', 'correto'),
        ('Ela tem muitas roupas', 'correto'),
        ('Eu comprei um celular novo', 'correto'),
        ('Estou com saudades dos meus amigos', 'correto'),
        ('Ela gosta de cozinhar', 'correto'),
        ('Ele prefere nadar do que correr', 'correto'),
        ('Eu sou um desenvolvedor de software', 'correto'),
        ('Eles foram ao parque', 'correto'),
        ('Eu falo portugues fluentemente', 'correto'),
        ('Ela não gosta de dormir cedo', 'correto'),
        ('Eu quero aprender mais sobre Machine Learning', 'correto'),
        ('Eles foram jantar fora', 'correto'),
        ('Este livro é um best-seller', 'correto'),
        ('Ela adora sorvete de morango', 'correto'),
        ('Eu gosto de ler romances', 'correto'),
        ('Eles vão ao cinema toda semana', 'correto'),
        ('Este restaurante é muito bom', 'correto'),
        ('Ela não tem tempo para isso', 'correto'),
        ('Eu não gosto de acordar cedo', 'correto'),
        ('Eles moram perto do parque', 'correto'),
        ('Este é um problema difícil', 'correto'),
        ('Ela não gosta de estudar', 'correto'),
        ('Eu adoro música', 'correto'),
        ('Eles foram à praia', 'correto'),
        ('Este programa é muito útil', 'correto'),
        ('Ela'),
    ]


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


if __name__ == '__main__':    # pragma: no cover
    run()
