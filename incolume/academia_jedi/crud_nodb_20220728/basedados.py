from .model import Pessoa


db = {}


def create(pessoa: Pessoa):
    db[pessoa.id] = pessoa
    return True


def update(id:int, pessoa: Pessoa):
    if db.get(id):
        db.update({id: pessoa})
        return True
    return False


def delete(id: int):
    if db.get(id):
        db.pop(id)
        return True
    return False


def select_all():
    return [pessoa for key, pessoa in db.items()]


def select(id: int):
    return db.get(id)

