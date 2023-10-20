import re
from collections import namedtuple


def tratativa():
    pattern = re.compile(
        r"""(?x)
        (?P<float>\d+\.\d+) |
        (?P<int>\d+) |
        (?P<variable>\w+) |
        (?P<string>".*")
    """,
    )
    Token = namedtuple('Token', ('kind', 'value', 'position'))
    env = {'x': 'hello', 'y': 10}

    for s in ['123', '123.45', 'x', 'y', '"goodbye"']:
        mo = pattern.fullmatch(s)
        match mo.lastgroup:
            case 'float':
                tok = Token('NUM', float(s), mo.span())
            case 'int':
                tok = Token('NUM', int(s), mo.span())
            case 'variable':
                tok = Token('VAR', env[s], mo.span())
            case 'string':
                tok = Token('TEXT', s[1:-1], mo.span())
            case _:
                msg = f'Unknown pattern for {s!r}'
                raise ValueError(msg)
        print(tok)


def run():
    tratativa()


if __name__ == '__main__':  # pragma: no cover
    run()
