"""Modulo para manipulação de arquivos."""

from pathlib import Path
import csv
from pprint import pprint
import json
import xlsxwriter
from typing import Final 

CONTENT: Final = [
    {'id': 1, 'nome': 'ciclano', 'telefone': '614235-6789'},
    {'id': 2, 'nome': 'fulano', 'telefone': '617546-4512'},      
    {'id': 3, 'nome': 'beltrano', 'telefone': '621427-7546'},      
    {'id': 4, 'nome': 'josé da silva', 'telefone': '614215-7645'},
    {'id': 5, 'nome': 'joão da silva', 'telefone': '617777-7777'},
    {'id': 6, 'nome': 'sabino cruz das colves', 'telefone': '(61) 95555-5555'},
]


def exemplo1(fl: Path):
    """Modo de criação 1."""
    file = open(fl.name, 'w')
    file.write('alguma coisa')
    file.close()


def exemplo2(fl: Path):
    """Exemplo 2."""
    file = open(fl.name, 'w')
    file.write('alguma coisa\n')
    file.write('outra coisa')
    file.close()


def exemplo3(fl: Path):
    """"""
    with open(fl.name, 'w') as file:
        file.write('alguma coisa.')


def exemplo4():
    """"""
    file = Path('arquivo4.txt')
    file.write_text('alguma coisa')


def exemplo5():
    """exemplo contexto + pathlib + TXT."""
    with Path('arquivo5.txt').open('w') as file:
        file.write('alguma coisa')
        file.write('outra coisa')


def exemplo6(file: Path) -> None:
    """CSV."""
    # print(file.is_file())
    with open(file.as_posix(), newline='') as csvfile:
        handler = csv.reader(csvfile, delimiter=';')
        for linha in handler:
            print(linha)


def exemplo7(file: Path) -> None:
    """CSV."""
    # print(file.is_file())
    with open(file.as_posix(), newline='') as csvfile:
        handler = csv.reader(csvfile, delimiter=';')

        title = next(handler)
        print(title)

        for linha in handler:
            print(linha)


def exemplo8() -> None:
    """CSV."""
    file = Path(__file__).absolute().parent.parent.parent.parent / 'xpto.csv'
    # print(file.is_file())
    with open(file.as_posix(), newline='') as csvfile:
        handler = csv.reader(csvfile, delimiter=';')

        title = next(handler)
        print(title)

        for linha in handler:
            print(list(zip(title, linha)))


def exemplo9() -> None:
    """CSV."""
    file = Path(__file__).absolute().parent.parent.parent.parent / 'xpto.csv'
    # print(file.is_file())
    with open(file.as_posix(), newline='') as csvfile:
        handler = csv.reader(csvfile, delimiter=';')

        title = next(handler)
        # print(title)

        d = []
        for linha in handler:
            d.append(dict(zip(title, linha)))
        pprint(d)


def exemplo10() -> None:
    """CSV."""
    file = Path(__file__).absolute().parent.parent.parent.parent / 'xpto.csv'
    # print(file.is_file())
    with open(file.as_posix(), newline='') as csvfile:
        
        handler = csv.DictReader(csvfile, delimiter=';')
        for linha in handler:
            print(linha)


def exemplo11() -> None:
    """exemple escreve JSON."""

    with open('exemplo11.json', 'w') as jsonfile:
        json.dump(CONTENT, jsonfile, indent=4)


def exemplo12() -> None:
    """exemplo lê JSON."""
    with open('exemplo11.json') as jsonfile:
        content = json.load(jsonfile)
    for record in content:
        print(record)


def exemplo13() -> None:
    """Exemplo XLSX com modulo xlsxwriter."""

    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('exemplo13.xlsx')
    worksheet = workbook.add_worksheet()
    # Start from the first cell. Rows and columns are zero indexed.
    row = 0
    col = 0
    # print(content)
    # Iterate over the data and write it out row by row.
    for content in CONTENT:
        for key, value in content.items():
            # print(key, value)
            worksheet.write(row, col,     key)
            worksheet.write(row, col + 1, value)
            row += 1
    workbook.close()    


def run() -> None:
    """"""
#    exemplo1()
#    exemplo2()
#    exemplo3()
#    exemplo4()
#    exemplo5()
#    exemplo6(Path(__file__).absolute().parent.parent.parent.parent / 'xpto.csv')
#    exemplo7(Path(__file__).absolute().parent.parent.parent.parent / 'xpto.csv')
#    exemplo11()
#    exemplo12()
    exemplo13()
    


if __name__ == '__main__':
    run()