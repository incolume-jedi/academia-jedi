import contextlib

# ruff: noqa: D100, D419, F841
import io


def run():
    """"""
    with contextlib.redirect_stdout(zen := io.StringIO()):
        import this

        return this.s, this.d


if __name__ == '__main__':
    print(run())
