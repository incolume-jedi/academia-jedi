import contextlib
import io
import sys
import platform


if sys.version_info < (3, 8):
    raise Exception(
        f"Incompatible python version. Current {platform.python_version()}. minimal Python 3.8+"
    )


def run():
    with contextlib.redirect_stdout(zen := io.StringIO()):
        import this

        return zen.getvalue()


if __name__ == "__main__":
    print(run())
