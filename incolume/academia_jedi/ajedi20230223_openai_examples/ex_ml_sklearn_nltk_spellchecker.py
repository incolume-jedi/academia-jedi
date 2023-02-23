import re
from spellchecker import SpellChecker
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Carrega o corretor ortográfico
spell = SpellChecker()

# Define um conjunto de textos para treinamento
textos_treinamento = [
    "Eu sempre gosto de correr no parque",
    "Eu gosto de laranjas, mas não de maçãs",
    "A música é minha paixão desde que eu era criança",
    "O cachorro late o dia todo no quintal",
    "A matemática é uma ciência fascinante"
]

# Extrai as palavras dos textos de treinamento
palavras_treinamento = [word_tokenize(texto.lower()) for texto in textos_treinamento]

# Cria um vetor de características com as palavras únicas dos textos de treinamento
vetorizador = CountVectorizer(tokenizer=lambda doc: doc, lowercase=False)
vetor_caracteristicas = vetorizador.fit_transform(palavras_treinamento)

# Cria um modelo de classificação para prever se uma palavra está correta ou não
modelo = LogisticRegression(max_iter=5000)
y_treinamento = [
    1 if palavra in spell else 0
    for texto in palavras_treinamento for palavra in texto]
modelo.fit(vetor_caracteristicas, y_treinamento)

# Define o texto para correção
texto = "Ela comprou uma blusa azul no shoping"

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
            palavras[i] = spell.correction(palavra) if not sugestoes else sugestoes[0]

# Concatena as palavras corrigidas para formar o texto corrigido
texto_corrigido = " ".join(palavras)

# Imprime o texto corrigido
print(texto_corrigido)
