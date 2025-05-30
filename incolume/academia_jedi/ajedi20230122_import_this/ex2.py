import contextlib

# ruff: noqa: D100, D103, T201
import io


def run():
    with contextlib.redirect_stdout(zen := io.StringIO()):
        return zen.getvalue()


if __name__ == '__main__':
    print(run())
