"""Calculadora CLI."""

# ruff: noqa: T201

import os
from collections.abc import Container
from enum import Enum, unique, IntEnum

Options: Enum = unique(
    IntEnum(
        value='Options',
        names=[
            'Sair',
            'Soma',
            'Subtração',
            'Multiplicação',
            'Divisão',
            'Exponenciação',
        ],
        start=0,
    ),
)


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
        match op:
            case '0':
                break
            case _:
                print('\n\tOpção inválida!\n')
        print('-' * 30)
        if finalizar(
            'deseja realizar outra operação (Y/n)? ',
            ['f', 'finalize', 't', 'terminar'],
        ):
            break


if __name__ == '__main__':
    menu()
