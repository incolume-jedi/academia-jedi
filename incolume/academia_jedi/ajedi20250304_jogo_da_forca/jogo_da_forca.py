"""Jogo da forca module."""

from pathlib import Path

from tomli import load

# ruff:noqa:T201
alfabeto = 'abcdefghijklmnopqrstuvxwyz'

chances = 6

palavras_db = Path(__file__).parent / 'palavras.toml'


def cabecalho():
    """Header."""
    print('=' * 90)
    print('Jogo da Forca'.center(90))
    print('=' * 90)
    print('Bem vindo! Aperte "ENTER" para começar.')
    print('-' * 90)
    input()
    print('Que comecem os jogos!!!!')


def menu(arquivo_palavras: (str | Path)) -> list[str]:
    """Menu.

    Args:
        arquivo_palavras (str  |  Path): arquivo de base de dados para jogo

    Returns:
        list[str]: palavras
    """
    with Path(arquivo_palavras).open('rb') as file:
        palavras = load(file)
    for opcao in palavras:
        print(f'* {opcao}')
    op = input('Digite uma das opções disponíveis: ')
    return palavras.get(op)


def run():
    """Run it."""
    # cabecalho()
    # print(alfabeto)
    # print(chances)
    # for letra in alfabeto:
    #     print(letra)
    # escolha = input('Digite uma letra do alfabeto: ').lower()
    # print(escolha)
    # print(escolha == "b")
    # with Path('palavras.toml').open('rb') as file:
    #     print(load(file))
    palavras = menu(palavras_db)
    print(palavras)


if __name__ == '__main__':  # pragma: no cover
    run()
