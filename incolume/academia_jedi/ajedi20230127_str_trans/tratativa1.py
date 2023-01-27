import contextlib
import io
import sys
from functools import namedtuple


if sys.version_info < (3, 8):
    raise Exception(f'Incompatible python version. Current {platform.python_version()}. minimal Python 3.8+')



def elements_this():
    """"""
    element = namedtuple('this', 'encript dict text')
    with contextlib.redirect_stdout(zen := io.StringIO()):
        import this
        return element(this.s, this.d, zen.getvalue())


if __name__ == '__main__':
    print(elements_this())