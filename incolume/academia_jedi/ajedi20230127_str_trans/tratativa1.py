import contextlib

# ruff: noqa: D100, D419, PYI024, T201
import io
from collections import namedtuple


def elements_this():
    """"""
    element = namedtuple('this', 'encript dict text')
    with contextlib.redirect_stdout(zen := io.StringIO()):
        import this

        return element(this.s, this.d, zen.getvalue())


if __name__ == '__main__':
    print(elements_this())
