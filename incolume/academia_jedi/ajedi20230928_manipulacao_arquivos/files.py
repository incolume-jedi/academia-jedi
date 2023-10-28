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


def exemplo01(fl: Path):
    """Modo de criação 1."""
    file = open(fl.as_posix(), 'w')
    file.write('alguma coisa')
    file.close()


def exemplo02(fl: Path):
    """Exemplo 2."""
    file = open(fl.as_posix(), 'w')
    file.write('alguma coisa\n')
    file.write('outra coisa')
    file.close()


def exemplo03(fl: Path):
    """"""
    with open(fl.as_posix(), 'w') as file:
        file.write('alguma coisa.')


def exemplo04(file: Path):
    """"""
    file.write_text('alguma coisa')


def exemplo05(fl: Path):
    """exemplo contexto + pathlib + TXT."""
    with fl.open('w') as file:
        file.write('alguma coisa')
        file.write('outra coisa')


def exemplo06(file: Path = None) -> None:
    """CSV write.
    Criação de CSV a partir de dict.
    """
    file = file or Path('names.csv')
    with open(file.as_posix(), 'w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
        writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
        writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


def exemplo07(file: Path = None, data: list[dict] = None) -> None:
    """CSV write."""
    file = file or Path('names.csv')
    data = data or CONTENT
    with open(file.as_posix(), 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        [writer.writerow(record) for record in data]


def exemplo08(file: Path) -> None:
    """CSV read."""
    # print(file.is_file())
    with open(file.as_posix(), newline='') as csvfile:
        handler = csv.reader(csvfile, delimiter=';')
        for linha in handler:
            print(linha)


def exemplo08(file: Path) -> None:
    """CSV."""
    # print(file.is_file())
    with open(file.as_posix(), newline='') as csvfile:
        handler = csv.reader(csvfile, delimiter=';')

        title = next(handler)
        print(title)

        for linha in handler:
            print(linha)


def exemplo09() -> None:
    """CSV."""
    file = Path(__file__).absolute().parent.parent.parent.parent / 'xpto.csv'
    # print(file.is_file())
    with open(file.as_posix(), newline='') as csvfile:
        handler = csv.reader(csvfile, delimiter=';')

        title = next(handler)
        print(title)

        for linha in handler:
            print(list(zip(title, linha)))


def exemplo10() -> None:
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
    # exemplo01()
    # exemplo02()
    # exemplo03()
    # exemplo04(file = Path('arquivo4.txt'))
    # exemplo05()
    exemplo06()
    exemplo07(Path(__file__).absolute().parents[0] / 'xpto.csv')
    # exemplo08(Path(__file__).absolute().parent.parent.parent.parent / 'xpto.csv')
    # exemplo11()
    # exemplo12()
    # exemplo13()


if __name__ == '__main__':
    run()
