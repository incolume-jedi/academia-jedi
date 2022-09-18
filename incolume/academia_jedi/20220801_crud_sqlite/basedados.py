import logging
from model import Pessoa
from pathlib import Path
import logging
import sqlite3

logging.basicConfig(level=logging.WARNING)
file_sqlite = Path('pessoas.sqlite')


con = sqlite3.connect(file_sqlite)
cur = con.cursor()
USER_DDL = 'CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, date_born DATETIME NOT NULL)'
EMAIL_DDL = '''CREATE TABLE IF NOT EXISTS emails(
    email_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER, email TEXT NOT NULL,
    CONSTRAINT fk_users FOREIGN KEY (user_id)
    REFERENCES users(user_id))'''
TEL_DDL = '''CREATE TABLE IF NOT EXISTS telefones(
    telefone_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    telefone TEXT NOT NULL,
    CONSTRAINT fk_users FOREIGN KEY (user_id)
    REFERENCES users(user_id))'''
ADD_DDL = '''CREATE TABLE IF NOT EXISTS addresses(
    address_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    address TEXT NOT NULL,
    CONSTRAINT fk_users FOREIGN KEY (user_id)
    REFERENCES users(user_id))'''

db = {}

def debug_mode(status: bool = False):
    if status:
        logging.basicConfig(level=logging.DEBUG)

def create_person(pessoa: Pessoa, debug: bool = False):
    debug_mode(debug)
    cur.execute(USER_DDL)
    cur.execute(EMAIL_DDL)
    cur.execute(TEL_DDL)
    cur.execute(ADD_DDL)
    # db[pessoa.id] = pessoa
    # logging.debug(f'Adicionado: {pessoa.__dict__}')
    return True


def update_person(id:int, pessoa: Pessoa):
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
    return [pessoa for _, pessoa in db.items()]


def select_person(id: int):
    return db.get(id)
