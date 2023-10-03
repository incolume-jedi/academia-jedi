import re
from dataclasses import dataclass


class MyPatterns:
    ALPHA = re.compile(r'\w+')
    WHITESPACES = re.compile(r'\s+')
    DIGITS = re.compile(r'\d+')


# noinspection PyPep8Naming


@dataclass
class regex_in:
    string: str

    def __eq__(self, other: str | re.Pattern):
        if isinstance(other, str):
            other = re.compile(other)
        assert isinstance(other, re.Pattern)
        # TODO extend for search and match variants
        return other.fullmatch(self.string) is not None


def tratativa1(validated_string):
    match regex_in(validated_string):
        case MyPatterns.DIGITS:
            print("This works, it's all digits")
        case MyPatterns.WHITESPACES:
            print('Whitespaces detected.')
        case MyPatterns.ALPHA:
            print('Alphanumeric detected.')
        case _:
            print('Do not match!')


def run():
    itens = [
        'abc4',
        '123',
        '   ',
    ]
    for item in itens:
        tratativa1(item)


if __name__ == '__main__':  # pragma: no cover
    run()
