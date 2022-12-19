from basic_use import create_eg
from platform import python_version

if python_version() < '3.11.0':
    print("This application need Python 3.11+")
    exit(1)

if __name__ == '__main__':    # pragma: no cover
    # create_eg()

    try:
        create_eg()
    except* ValueError as e:
        for error in e.exceptions:
            print(error)
    except* FileNotFoundError as e:
        for error in e.exceptions:
            print(error)
