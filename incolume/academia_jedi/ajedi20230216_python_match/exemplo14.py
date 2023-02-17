import re
from dataclasses import dataclass


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
        case r'\d+':
            print('Digits')
        case r'\s+':
            print('Whitespaces')
        case _:
            print('Something else')


def run():
    itens = [
        'abc',
        '123',
        '   ',
    ]
    for item in itens:
        tratativa1(item)


if __name__ == '__main__':    # pragma: no cover
    run()
