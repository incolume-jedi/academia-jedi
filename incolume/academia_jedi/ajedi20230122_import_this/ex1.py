import contextlib
import io


def run():
    zen = io.StringIO()
    with contextlib.redirect_stdout(zen):
        pass

    return zen.getvalue()


if __name__ == '__main__':
    print(run())
