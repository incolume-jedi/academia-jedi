"""Unificado a partir do arquivo:
incolume/academia_jedi/ajedi20220928_morsa_op/main.py
"""

__author__ = '@britodfbr'  # pragma: no cover


def menu():
    """Operador morsa."""
    while (op := input('Escolha um numero (zero (0) para sair): ')) != '0':
        print(op)


def run():
    menu()


if __name__ == '__main__':  # pragma: no cover
    run()
