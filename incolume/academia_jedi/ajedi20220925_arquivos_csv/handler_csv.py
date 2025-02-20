# !/usr/bin/env python

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
__author__ = '@britodfbr'  # pragma: no cover
import csv
import logging

from incolume.academia_jedi.ajedi20220925_massa_dados_faker_protocol.generator_pessoas import (
    massa_pessoas,
)

logFormat = (
    '%(asctime)s; %(levelname)-8s; %(name)s; %(module)s;'
    ' %(funcName)s; %(threadName)s; %(thread)d; %(message)s'
)
logging.basicConfig(level=logging.DEBUG, format=logFormat)


def csv_0():
    """Exemplo criação de CSV a partir de listas."""
    with open('eggs.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(
            csvfile,
            delimiter=' ',
            quotechar='|',
            quoting=csv.QUOTE_MINIMAL,
        )
        spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


def csv_1():
    """Exemplo leitura de CSV."""
    with open('eggs.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(', '.join(row))


def csv_2():
    """Criação de CSV a partir de dict."""
    with open('names.csv', 'w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
        writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
        writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


def csv_3():
    with open('names.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            logging.debug(row)
            logging.debug('{} {}'.format(row['first_name'], row['last_name']))


def csv_4_write_pessoas():
    """Gravar pessoas em CSV."""
    pessoas = massa_pessoas()
    for pessoa in pessoas:
        logging.debug(pessoa.__dict__)

    with open('pessoas.csv', 'w', newline='') as csvfile:
        fieldnames = pessoas[0].__dict__.keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for pessoa in pessoas:
            writer.writerow(pessoa.__dict__)


def csv_5_read_pessoas():
    with open('pessoas.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            logging.debug(row)


def run():
    csv_0()
    csv_1()
    csv_2()
    csv_3()
    csv_4_write_pessoas()
    csv_5_read_pessoas()


if __name__ == '__main__':  # pragma: no cover
    run()
