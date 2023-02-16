import shelve
from incolume.academia_jedi.ajedi20220925_massa_dados_faker_protocol.\
    generator_pessoas import massa_pessoas, Pessoa
from pathlib import Path
import dotenv
import logging
import os

__author__ = "@britodfbr"  # pragma: no cover

config = dotenv.load_dotenv(dotenv.find_dotenv())
logging.debug(config)

dados = massa_pessoas(is_json=False)
logging.debug(dados)

fileoutput = Path(__file__).parent / 'databases'/os.getenv('BASENAME')
fileoutput.parent.mkdir(exist_ok=True, parents=True)
logging.debug(fileoutput)


def ex01():
    """Gravar dados em shelve file."""
    with shelve.open(fileoutput.as_posix()) as db:
        db['a'] = 1
        db['b'] = 2
        db['c'] = 3
        db['d'] = 4
        logging.debug(dict(db.items()))


def ex02():
    """Ler dados em shelve file."""
    with shelve.open(fileoutput.as_posix()) as db:
        print(
            dict(db.items()),
            type(db),
            db.get('a'),
            sep='\n'
        )
        logging.debug(db.items())


def ex03():
    """Atualizar dados em shelve file."""
    data: dict = {'f': 1, 'a': 5}
    with shelve.open(fileoutput.as_posix()) as db:
        db.update(data)
        logging.debug(dict(db.items()))


def ex04():
    """Objetos em shelve file."""
    file = fileoutput.with_name('Obj').as_posix()
    with shelve.open(file) as db:
        db['0'] = dados[0]
        logging.debug(dict(db.items()))

    with shelve.open(file) as db:
        print(dict(db.items()))


def ex05():
    """Objetos em shelve file."""
    file = fileoutput.with_name('Obj2').as_posix()
    with shelve.open(file) as db:
        for i, data in enumerate(dados):
            db[str(i)] = data
        logging.debug(dict(db.items()))

    with shelve.open(file) as db:
        print(dict(db.items()))


def run():
    logging.debug('running..')
    ex01()
    ex02()
    ex03()
    ex02()
    ex04()
    ex05()


if __name__ == '__main__':    # pragma: no cover
    run()
