"""Module."""

import sys
from platform import python_version

from incolume.academia_jedi.ajedi20221219_Como_Usar_ExceptionsGroups.basic_use import (
    create_eg,
)

if python_version() < '3.11.0':
    sys.exit('This application need Python 3.11+')

if __name__ == '__main__':  # pragma: no cover
    try:
        create_eg()
    except* ValueError as e:
        for error in e.exceptions:
            print(error)
    except* FileNotFoundError as e:
        for error in e.exceptions:
            print(error)
