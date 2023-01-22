import googletrans
from googletrans import Translator

__author__ = "@britodfbr"  # pragma: no cover
translator = Translator()


def languages_list():
    print(googletrans.LANGUAGES)


def translate_example1():
    result = [
        translator.translate('Mitä sinä teet'),
        translator.translate('Mikä on nimesi', src='fi'),
        translator.translate('Mikä on nimesi', src='fi', dest='pt'),
    ]

    for frase in result:
        print(frase.src)
        print(frase.dest)
        print(frase.origin, frase.text)


def run():
    languages_list()
    translate_example1()


if __name__ == '__main__':    # pragma: no cover
    run()
