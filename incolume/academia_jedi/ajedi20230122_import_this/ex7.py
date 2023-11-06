import contextlib
import io


def run():
    """"""
    with contextlib.redirect_stdout(zen := io.StringIO()):
        import this

        return this.s, this.d, zen.getvalue()


if __name__ == '__main__':
    print(run())
