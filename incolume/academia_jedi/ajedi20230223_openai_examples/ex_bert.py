from transformers import pipeline

# Configura o analisador de sentimentos do BERT
sentiment_classifier = pipeline(
    'sentiment-analysis', model='bert-base-uncased',
)

# Analisa o sentimento de uma frase
result = sentiment_classifier('I love pizza')[0]

# Imprime o resultado
print(result['label'], result['score'])
