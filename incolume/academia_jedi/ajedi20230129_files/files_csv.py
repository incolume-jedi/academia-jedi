import csv
import logging
from config import config, fileoutput, dados_dict
from incolume.academia_jedi.ajedi20230211_massa_dados_faker_protocol.models import (
    Pessoa,
)

__author__ = '@britodfbr'  # pragma: no cover

logging.debug(config)
logging.debug(fileoutput)


def ex1():
    """Create CSV file."""
    logging.debug(dados_dict)
    logging.debug(Pessoa.__annotations__.keys())
    with fileoutput.with_suffix('.csv').open('w') as file:
        handler_csv = csv.DictWriter(
            file, fieldnames=Pessoa.__annotations__.keys()
        )
        handler_csv.writeheader()
        handler_csv.writerows(dados_dict)


def ex2():
    """Read CSV file.
    A partir de dicionário.
    """
    with fileoutput.with_suffix('.csv').open() as file:
        handler_csv = csv.DictReader(file)
        logging.debug(handler_csv)
        for person in handler_csv:
            print(person)


def run() -> None:
    ex1()
    ex2()


if __name__ == '__main__':  # pragma: no cover
    run()
