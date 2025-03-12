"""Package."""

from unidecode import unidecode

__author__ = '@britodfbr'  # pragma: no cover

# ruff: noqa: T201

words = [
    'missíssipi',
    'abracadabra',
    'açaí',
    'água',
]


def mapping_letters1():  # pragma: no cover
    """Implementation #1."""
    for word in words:
        print(word, unidecode(word))


def mapping_letters2():  # pragma: no cover
    """Implementation #2."""
    for word in (unidecode(w) for w in words):
        print(word)


def mapping_letters3():  # pragma: no cover
    """Implementation #2."""
    for word in (unidecode(w) for w in words):
        d = {}
        print(word, end=' ')
        for index, letter in enumerate(word):
            d.setdefault(letter, []).append(index)
        print(d)


def mapping_letters(text: str = '') -> dict[str, list[int]]:
    """Solution."""
    result = {}
    for index, letter in enumerate(text):
        result.setdefault(letter, []).append(index)
    return result


def run():
    """Run it."""
    funcs = [
        mapping_letters1,
        mapping_letters2,
        mapping_letters3,
    ]
    for func in funcs:
        print(func.__name__)
        func()
        print()


if __name__ == '__main__':  # pragma: no cover
    run()
