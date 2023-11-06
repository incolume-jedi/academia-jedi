import re
from collections import namedtuple


def tratativa():
    pattern = re.compile(r'(\d+\.\d+)|(\d+)|(\w+)|(".*)"')
    Token = namedtuple('Token', ('kind', 'value', 'position'))
    env = {'x': 'hello', 'y': 10}

    for s in ['123', '123.45', 'x', 'y', '"goodbye"']:
        mo = pattern.fullmatch(s)
        match mo.lastindex:
            case 1:
                tok = Token('NUM', float(s), mo.span())
            case 2:
                tok = Token('NUM', int(s), mo.span())
            case 3:
                tok = Token('VAR', env[s], mo.span())
            case 4:
                tok = Token('TEXT', s[1:-1], mo.span())
            case _:
                msg = f'Unknown pattern for {s!r}'
                raise ValueError(msg)
        print(tok)


def run():
    tratativa()


if __name__ == '__main__':  # pragma: no cover
    run()
