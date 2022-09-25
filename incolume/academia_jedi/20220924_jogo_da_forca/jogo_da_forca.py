# !/usr/bin/env python
# -*- coding: utf-8 -*-
from tomli import load
from pathlib import Path

alfabeto = 'abcdefghijklmnopqrstuvxwyz'

chances = 6


def cabecalho():
    print('=' * 90)
    print("Jogo da Forca".center(90))
    print('=' * 90)
    print('Bem vindo! Aperte "ENTER" para começar.')
    print('-' * 90)
    input()
    print('Que comecem os jogos!!!!')


def menu(arquivo_palavras: (str | Path)):
    with Path(arquivo_palavras).open('rb') as file:
        palavras = load(file)
    for opcao in palavras.keys():
        print(f"* {opcao}")
    op = input('Digite uma das opções disponíveis:')
    return palavras.get(op)


def run():
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
    palavras = menu('palavras.toml')
    print(palavras)
    pass


if __name__ == '__main__':  # pragma: no cover
    ...
    run()
