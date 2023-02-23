from spellchecker import SpellChecker

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

