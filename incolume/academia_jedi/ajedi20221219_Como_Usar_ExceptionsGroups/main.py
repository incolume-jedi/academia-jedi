from basic_use import create_eg

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
