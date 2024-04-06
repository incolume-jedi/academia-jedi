# !/usr/bin/env python
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
