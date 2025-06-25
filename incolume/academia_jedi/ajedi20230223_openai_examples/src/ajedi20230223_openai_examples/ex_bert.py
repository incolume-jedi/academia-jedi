"""Module estudo com transformers."""

import contextlib
import sys

if not ((3, 8) < sys.version_info < (3, 11)):
    with contextlib.suppress(SystemExit):
        sys.exit('This application need Python 3.8+ and below 3.11')
else:
    from transformers import pipeline


def example01():
    """Example."""
    # Configura o analisador de sentimentos do BERT
    sentiment_classifier = pipeline(
        'sentiment-analysis',
        model='bert-base-uncased',
    )

    # Analisa o sentimento de uma frase
    result = sentiment_classifier('I love pizza')[0]

    # Imprime o resultado
    print(result['label'], result['score'])


if __name__ == '__main__':
    example01()
