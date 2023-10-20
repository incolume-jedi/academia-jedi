from collections import Counter

from spellchecker import SpellChecker

# Carrega o corretor ortográfico
spell = SpellChecker()

# Define o texto para correção
texto = 'Esse sit é muito legau'

# Separa as palavras do texto
palavras = texto.split()


# Define uma função para gerar sugestões de correção
def sugestoes_correcao(palavra):
    # Sugestões de correção com base no PySpellChecker
    sugestoes = spell.candidates(palavra)

    # Probabilidades de correção com base no algoritmo de Peter Norvig
    probabilidades = Counter()
    n = sum(probabilidades.values())

    # Implementação do algoritmo de Peter Norvig
    for c in spell.edit_distance_1(palavra):
        for w in spell.candidates(c):
            probabilidades[w] += spell.word_probability(w) / n

    # Retorna as sugestões de correção ordenadas por probabilidade
    return [
        sugestao for sugestao in probabilidades if sugestao in sugestoes
    ]


# Corrige a ortografia de cada palavra
for i, palavra in enumerate(palavras):
    # Verifica se a palavra está escrita corretamente
    if spell.correction(palavra) != palavra:
        # Gera sugestões de correção
        sugestoes = sugestoes_correcao(palavra)
        # Se houver sugestões de correção, substitui a palavra no texto
        if sugestoes:
            palavras[i] = sugestoes[0]

# Concatena as palavras corrigidas para formar o texto corrigido
texto_corrigido = ' '.join(palavras)

# Imprime o texto corrigido
print(texto_corrigido)
