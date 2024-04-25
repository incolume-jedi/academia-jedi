from datetime import datetime


def example01() -> None:
    """Formatar datetime (local time).

    Formatar em string com milissegundos (2022-10-03 11:41:07.916)
    """
    print(
        datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3],
        datetime.now().isoformat(sep=' ', timespec='milliseconds'),
        datetime.now().strftime('%F %T.%f')[:-3],
        sep='\n',
        end='\n\n',
    )


def example02() -> None:
    """Formatar datetime (UTC).

    Formatar datetime UTC em string com milissegundos
    (2022-10-03 11:41:07.916)'
    """
    print(
        datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3],
        datetime.utcnow().isoformat(sep=' ', timespec='milliseconds'),
        datetime.utcnow().strftime('%F %T.%f')[:-3],
        sep='\n',
        end='\n\n',
    )


def example03() -> None:
    """Formatar timestamp em formato ISO8601."""
    print(
        datetime.now().strftime('%FT%T'),
        datetime.now().strftime('%FT%T.%f'),
        datetime.now().isoformat(timespec='milliseconds'),
        sep='\n',
    )


def run():
    example01()
    example02()
    example03()


if __name__ == '__main__':  # pragma: no cover
    run()
