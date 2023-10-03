"""Matching Builtin Types."""
import builtins
from typing import Any


def classifier(value: Any):
    """"""
    match value:
        case float():  # Correct!
            print(f'{value} is float')
        case _:
            print(f'"{value}" not is float!')


def match_builtins(type_):
    """Matches raw types, not their instances."""
    match type_:
        case builtins.str:
            print(f'{type_} is a String.')
        case builtins.int:
            print(f'{type_} is an Integer.')
        case _:
            print(f'{type_} Invalid type.')


def run():
    some_var = ['not a float', 3.14]
    for value in some_var:
        classifier(value)

    some_types = [int, str, list, tuple]
    for value in some_types:
        match_builtins(value)


if __name__ == '__main__':  # pragma: no cover
    run()
