"""Solving question."""
import logging

from incolume.academia_jedi.ajedi20220728_crud_nodb.model import Pessoa

logging.basicConfig(level=logging.WARNING)

db = {}


def debug_mode(status: bool = False):
    if status:
        logging.basicConfig(level=logging.DEBUG)


def create_person(pessoa: Pessoa, debug: bool = False):
    debug_mode(debug)
    db[pessoa.id] = pessoa
    logging.debug(f'Adicionado: {pessoa.to_dict()}')
    return True


def update_person(id: int, pessoa: Pessoa):
    if db.get(id):
        db.update({id: pessoa})
        return True
    return False


def delete_person(id: int):
    if db.get(id):
        db.pop(id)
        return True
    return False


def select_all_person():
    return [pessoa for key, pessoa in db.items()]


def select_person(id: int):
    return db.get(id)
