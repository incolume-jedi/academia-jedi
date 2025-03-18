"""Module."""
# ruff: noqa: T201

from datetime import datetime

from config import settings
from pytz import timezone


def example01() -> None:
    """Formatar datetime (local time).

    Formatar em string com milissegundos (2022-10-03 11:41:07.916)
    """
    print(
        datetime.now(timezone(settings.tz)).strftime('%Y-%m-%d %H:%M:%S.%f')[
            :-3
        ],
        datetime.now(timezone(settings.tz)).isoformat(
            sep=' ',
            timespec='milliseconds',
        ),
        datetime.now(timezone(settings.tz)).strftime('%F %T.%f')[:-3],
        sep='\n',
        end='\n\n',
    )


def example02() -> None:
    """Formatar datetime (UTC).

    Formatar datetime UTC em string com milissegundos
    (2022-10-03 11:41:07.916)'
    """
    print(
        datetime.now(timezone('UTC')).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3],
        datetime.now(timezone('UTC')).isoformat(
            sep=' ',
            timespec='milliseconds',
        ),
        datetime.now(timezone('UTC')).strftime('%F %T.%f')[:-3],
        sep='\n',
        end='\n\n',
    )


def example03() -> None:
    """Formatar timestamp em formato ISO8601."""
    print(
        datetime.now(timezone(settings.tz)).strftime('%FT%T'),
        datetime.now(timezone(settings.tz)).strftime('%FT%T.%f'),
        datetime.now(timezone(settings.tz)).isoformat(timespec='milliseconds'),
        sep='\n',
    )


def run():
    """Run it."""
    example01()
    example02()
    example03()


if __name__ == '__main__':  # pragma: no cover
    run()
