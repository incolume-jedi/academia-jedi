import dbm
import dotenv
import logging
from pathlib import Path
import os
from incolume.academia_jedi.ajedi20220925_massa_dados_faker_protocol.\
    generator_pessoas import massa_pessoas, Pessoa


__author__ = "@britodfbr"  # pragma: no cover


config = dotenv.load_dotenv(dotenv.find_dotenv())
logging.debug(config)


fileoutput = Path(__file__).parent / 'databases' / os.getenv('BASENAME')
fileoutput.parent.mkdir(exist_ok=True, parents=True)
logging.debug(fileoutput)

file = fileoutput.with_name(f'{fileoutput.stem}_people.dbm')
logging.debug(file)



def ex01():
    """dados em cache dbm."""
    logging.debug('..')
    
    # Open database, creating it if necessary.
    """
    Value|Meaning
    'r'| Open existing database for reading only (default)
    'w'| Open existing database for reading and writing
    'c'| Open database for reading and writing, creating it if it doesn’t exist
    'n'| Always create a new, empty database, open for reading and writing
    """
    with dbm.open('cache', 'c') as db:

        # Record some values
        db[b'hello'] = b'there'
        db['www.python.org'] = 'Python Website'
        db['www.cnn.com'] = 'Cable News Network'
        
        # Note that the keys are considered bytes now.
        assert db[b'www.python.org'] == b'Python Website'

        # Notice how the value is now in bytes.
        assert db['www.cnn.com'] == b'Cable News Network'

        # Often-used methods of the dict interface work too.
        print(db.get('python.org', 'not present'))
    # db is automatically closed when leaving the with statement.

def ex02():

        """
        # Storing a non-string key or value will raise an exception (most
        # likely a TypeError).
        """
        try:
            with dbm.open('cache', 'c') as db:
                db['www.yahoo.com'] = 4
        except TypeError as e:
            logging.error(e)


def ex03():
    """"""
    with dbm.open(file, 'c') as records:
        records['0'] = 'zero'
        records['1'] = 'um'
        records['2'] = 'dois'
        records['3'] = 'três'
        records['4'] = 'quatro'
    
    with dbm.open(file) as db:
        key = db.firstkey()
        print(f'{key=}{db.get(key)=}')
        nkey = db.nextkey(key)
        print(f'{nkey=}{db.get(nkey)=}')
        print(dict(db))


def ex04():
    """"""
    logging.debug('..')
    with dbm.dumb.open() as db:
        ...
        

def ex0x():
    """Gravar dados em arquivo dbm."""
    logging.debug('..')

    people = massa_pessoas(quantidade=3)

    print(people)

    with dbm.open(file, 'c') as f:
        logging.debug(type(f))
        for idx, person in enumerate(people):
            i = bytes(idx)
            f[i] = person

    # with dbm.open() as f:
    #     print(f)
    


def run():
    logging.debug('running..')
    ex01()
    ex02()
    ex03()


if __name__ == '__main__':    # pragma: no cover
    run()
