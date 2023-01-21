from platform import python_version

if python_version() < "3.11.0":
    print("This application need Python 3.11+")
    exit(1)


def create_eg():
    eg = ExceptionGroup(
        "Exception Group Message!",
        [
            FileNotFoundError("'anime.jpg' not found..."),
            FileNotFoundError("'anime.png' not found..."),
            FileNotFoundError("'icon.ico' not found..."),
            ValueError("'.git' not permited..."),
            ExceptionGroup("Nested exceptions", [ValueError("Not OK!")]),
        ],
    )
    raise eg


if __name__ == "__main__":  # pragma: no cover
    ...
