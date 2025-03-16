"""Calculadora CLI."""

# ruff: noqa: T201

import os
from collections.abc import Container
from enum import Enum, auto, unique
from operator import add, mul, pow, sub, truediv


@unique
class Options(Enum):
    """Option enum."""

    Sair = 0
    Soma = auto()
    Subtração = auto()
    Multiplicação = auto()
    Divisão = auto()
    Exponenciação = auto()

    @classmethod
    def _missing_(cls, value):
        if isinstance(value, str) and value.isdigit():
            value = int(value)
        else:
            value = value.capitalize()
        for member in cls:
            if value in (member.name, member.value):
                return member
        return None


def finalizar(
    msg: str = '',
    deny_options: None | Container[str] = None,
) -> bool:
    """Finalizar menu em loop."""
    deny: list[str] = ['não', 'no', 'n', 'q', 'quit', 'sair', 's']
    if deny_options:
        deny.extend(item.casefold() for item in deny_options)
    msg = msg or 'deseja realizar outra operação (Y/n)? '
    op = input(msg)
    return op.casefold() in deny


def limpar_tela() -> None:
    """Limpar tela."""
    os.system('cls' if os.name == 'nt' else 'clear')  # noqa: S605


def calc(
    x: float | None = None,
    y: float | None = None,
    op: Options | None = None,
    *,
    return_result: bool = False,
) -> float | None:
    """Realiza as operações da calculadora."""
    operador = {
        1: ('+', add),
        2: ('-', sub),
        3: ('*', mul),
        4: ('/', truediv),
        5: ('**', pow),
    }
    op = op or Options(1)

    msg = 'Opção inválida!'
    if op not in Options:
        if return_result:
            raise ValueError(msg)
        else:
            print(f'\n\t{msg}\n')
    x = x or float(input('Valor para x: '))
    y = y or float(input('Valor para y: '))
    result = operador.get(op.value)[1](x, y)
    if return_result:
        return result
    print(f'\n\n{x} {operador.get(op.value)[0]} {y} = {result}')
    return None


def menu():
    """Menu."""
    while True:
        limpar_tela()
        print('=' * 30)
        print(f'{"Calculadora CLI":^30}')
        print('-' * 30)
        for item in Options:
            print(f'   {item.value}: {item.name}')

        op = input('\nEscolha a opção que deseja realizar: ')

        calc(op=Options(op))

        print('-' * 30)

        if finalizar(
            'deseja realizar outra operação (Y/n)? ',
            ['f', 'finalize', 't', 'terminar'],
        ):
            break


if __name__ == '__main__':
    menu()
