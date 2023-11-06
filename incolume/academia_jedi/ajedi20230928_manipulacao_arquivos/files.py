"""Modulo para manipulação de arquivos."""

import csv
import json
from pathlib import Path
from pprint import pprint
from typing import Final

import xlsxwriter

CONTENT: Final = [
    {'id': 1, 'nome': 'ciclano', 'telefone': '614235-6789'},
    {'id': 2, 'nome': 'fulano', 'telefone': '617546-4512'},
    {'id': 3, 'nome': 'beltrano', 'telefone': '621427-7546'},
    {'id': 4, 'nome': 'josé da silva', 'telefone': '614215-7645'},
    {'id': 5, 'nome': 'joão da silva', 'telefone': '617777-7777'},
    {'id': 6, 'nome': 'sabino cruz das colves', 'telefone': '(61) 95555-5555'},
]


def exemplo01(fl: Path | None = None) -> None:
    """Modo de criação 1.

    write.
    """
    fl = fl or Path('exemplo01.txt')
    file = fl.open('w')
    file.write('alguma coisa')
    file.close()


def exemplo02(fl: Path | None = None) -> None:
    """Exemplo 2.

    write
    """
    fl = fl or Path('exemplo02.txt')
    file = fl.open('w')
    file.write('alguma coisa\n')
    file.write('outra coisa')
    file.close()


def exemplo03(fl: Path | None = None) -> None:
    """Exemplo3.

    Write com builtin open
    """
    fl = fl or Path('exemplo03.txt')
    with fl.open('w') as file:
        file.write('alguma coisa.')


def exemplo04(file: Path | None = None) -> None:
    """Exemplo4.

    Write com pathlib.
    """
    file = file or Path('exemplo04.txt')
    file.write_text('alguma coisa')


def exemplo05(fl: Path | None = None) -> None:
    """Exemplo write contexto + pathlib + TXT."""
    fl = fl or Path('exemplo05.txt')
    with fl.open('w') as file:
        file.write('alguma coisa')
        file.write('outra coisa')


def exemplo06(file: Path | None = None) -> None:
    """CSV write.

    Criação de CSV a partir de dict.
    """
    file = file or Path('names.csv')
    with file.open('w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
        writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
        writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


def exemplo07(
    file: Path | None = None,
    data: list[dict] | None = None,
) -> None:
    """CSV write."""
    file = file or Path('xpto.csv')
    data = data or CONTENT
    with file.open(mode='w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        _ = [writer.writerow(record) for record in data]


def exemplo08(file: Path | None = None) -> None:
    """CSV read."""
    file = file or Path('xpto.csv')
    with file.open(newline='') as csvfile:
        handler = csv.reader(csvfile, delimiter=';')
        for linha in handler:
            print(linha)  # noqa: T201


def exemplo09(file: Path | None = None) -> None:
    """CSV."""
    file = file or Path('xpto.csv')
    with file.open(newline='') as csvfile:
        handler = csv.reader(csvfile, delimiter=';')
        title = next(handler)
        print(title)  # noqa: T201

        for linha in handler:
            print(linha)  # noqa: T201


def exemplo10(file: Path | None = None) -> None:
    """CSV."""
    file = file or Path('xpto.csv')
    with file.open(newline='') as csvfile:
        handler = csv.reader(csvfile, delimiter=';')

        title = next(handler)
        print(title)  # noqa: T201

        for linha in handler:
            print(list(zip(title, linha, strict=True)))  # noqa: T201


def exemplo11(file: Path | None = None) -> None:
    """CSV."""
    file = file or Path('xpto.csv')
    with file.open(newline='') as csvfile:
        handler = csv.reader(csvfile, delimiter=';')

        title = next(handler)
        d = [dict(zip(title, linha, strict=True)) for linha in handler]
        pprint(d)  # noqa: T203


def exemplo12(file: Path | None = None) -> None:
    """CSV."""
    file = file or Path('xpto.csv')
    with file.open(newline='') as csvfile:
        handler = csv.DictReader(csvfile, delimiter=';')
        for linha in handler:
            print(linha)  # noqa: T201


def exemplo13(file: Path | None = None) -> list:
    """CSV."""
    file = file or Path('xpto.csv')
    with file.open(newline='') as csvfile:
        handler = csv.DictReader(csvfile, delimiter=';')
        return list(handler)


def exemplo14(
    file: Path | None = None,
    content: dict[str] | None = None,
) -> None:
    """Example write JSON."""
    file = file or Path('exemplo14.json')
    content = content or CONTENT
    with file.open('w') as jsonfile:
        json.dump(content, jsonfile, indent=4)


def exemplo15(file: Path | None = None) -> None:
    """Exemplo lê JSON."""
    file = file or Path('exemplo14.json')
    with file.open() as jsonfile:
        content = json.load(jsonfile)
    for record in content:
        print(record)  # noqa: T201


def exemplo16(file: Path | None = None) -> None:
    """Exemplo lê JSON."""
    file = file or Path('exemplo14.json')
    with file.open() as jsonfile:
        return json.load(jsonfile)


def exemplo17(file: Path | None = None) -> None:
    """Exemplo XLSX com modulo xlsxwriter."""
    file = file or Path('exemplo17.xlsx')
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook(file.as_posix())
    worksheet = workbook.add_worksheet()
    # Start from the first cell. Rows and columns are zero indexed.
    row = 0
    col = 0
    # Iterate over the data and write it out row by row.
    for content in CONTENT:
        for key, value in content.items():
            worksheet.write(row, col, key)
            worksheet.write(row, col + 1, value)
            row += 1
    workbook.close()


def exemplo18(file: Path | None = None) -> None:
    """Exemplo XLSX com modulo xlsxwriter."""
    file = file or Path('exemplo18.xlsx')
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook(file.as_posix())
    worksheet = workbook.add_worksheet()
    # Start from the first cell. Rows and columns are zero indexed.
    row = 0
    col = 0
    # Iterate over the data and write it out row by row.
    values = [list(CONTENT[0].keys())] + [x.values() for x in CONTENT]
    for content in values:
        for value in content:
            worksheet.write(row, col, value)
            col += 1
        col = 0
        row += 1
    workbook.close()


def run() -> None:
    """Run it."""
    exemplo01()
    exemplo02()
    exemplo03()
    exemplo04()
    exemplo05()
    exemplo06()
    exemplo07(Path(__file__).absolute().parents[0] / 'xpto.csv')
    exemplo08()
    exemplo09()
    exemplo10()
    exemplo11()
    exemplo12()
    exemplo13()
    exemplo14()
    exemplo15()
    exemplo16()
    exemplo17()
    exemplo18()


if __name__ == '__main__':
    run()
