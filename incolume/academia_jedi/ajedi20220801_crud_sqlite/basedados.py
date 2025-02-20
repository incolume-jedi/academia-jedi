import logging

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
import sqlite3
from pathlib import Path

from model import Pessoa

logging.basicConfig(level=logging.WARNING)
file_sqlite = Path('pessoas.sqlite')


con = sqlite3.connect(file_sqlite)
cur = con.cursor()
USER_DDL = 'CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, date_born DATETIME NOT NULL)'
EMAIL_DDL = """CREATE TABLE IF NOT EXISTS emails(
    email_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER, email TEXT NOT NULL,
    CONSTRAINT fk_users FOREIGN KEY (user_id)
    REFERENCES users(user_id))"""
TEL_DDL = """CREATE TABLE IF NOT EXISTS telefones(
    telefone_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    telefone TEXT NOT NULL,
    CONSTRAINT fk_users FOREIGN KEY (user_id)
    REFERENCES users(user_id))"""
ADD_DDL = """CREATE TABLE IF NOT EXISTS addresses(
    address_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    address TEXT NOT NULL,
    CONSTRAINT fk_users FOREIGN KEY (user_id)
    REFERENCES users(user_id))"""

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
    return [pessoa for _, pessoa in db.items()]


def select_person(id: int):
    return db.get(id)
