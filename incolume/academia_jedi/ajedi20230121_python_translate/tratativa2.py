from googletrans import Translator

__author__ = "@britodfbr"  # pragma: no cover
translator = Translator()

sentensas = (
    'Esta sentença está escrita em Português.'
    '이 문장은 한글로 쓰여졌습니다.',
    'この文章は日本語で書かれました。',
    'This sentence is written in English.',
    'Tiu frazo estas skribita en Esperanto.',
)


def ex01(frases):
    for frase in frases:
        return frase, translator.detect(frase)


def run():
    ex01(sentensas)


if __name__ == '__main__':  # pragma: no cover
    run()
