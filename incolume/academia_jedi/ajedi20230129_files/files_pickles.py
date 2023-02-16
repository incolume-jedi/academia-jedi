import pickle
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

file = fileoutput.with_name(f'{fileoutput.stem}_people.pkl')
logging.debug(file)



def ex01():
    """Gravar dados em arquivo pickle"""
    logging.debug('..')

    people = massa_pessoas(quantidade=3)

    with file.open('wb') as f:
        pickle.dump(people, f)

    with file.open('rb') as f:
        pessoas = pickle.load(f)
    for pessoa in pessoas:
        print(pessoa)

    


def run():
    logging.debug('running..')
    ex01()


if __name__ == '__main__':    # pragma: no cover
    run()
