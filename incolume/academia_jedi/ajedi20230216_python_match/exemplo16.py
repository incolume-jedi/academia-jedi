import re
from dataclasses import dataclass


# noinspection PyPep8Naming
@dataclass
class regex_in:
    string: str
    match: re.Match = None

    def __eq__(self, other: str | re.Pattern):
        if isinstance(other, str):
            other = re.compile(other)
        assert isinstance(other, re.Pattern)
        # TODO extend for search and match variants
        self.match = other.fullmatch(self.string)
        return self.match is not None

    def __getitem__(self, group):
        return self.match[group]


def tratativa(validated_string):
    # Note the `as m` in in the case specification
    match regex_in(validated_string):
        case r'\d(\d)\d' as m:
            print(f'The second digit is {m[1]}')
            print(f'The whole match is {m.match}')


def run():
    itens = [
        'abc4',
        '123',
        '   ',
    ]
    for item in itens:
        tratativa(item)


if __name__ == '__main__':  # pragma: no cover
    run()


