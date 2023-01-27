import contextlib
import io
import platform
import sys


if sys.version_info < (3, 6):
    raise Exception(f'Incompatible python version. Current {platform.python_version()}. minimal Python 3.6+')


def run():
    zen = io.StringIO()
    with contextlib.redirect_stdout(zen):
       import this

    return zen.getvalue()



if __name__ == '__main__':
    print(run())
