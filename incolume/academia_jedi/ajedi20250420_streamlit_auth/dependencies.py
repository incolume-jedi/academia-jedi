"""DB conection."""
# ruff: noqa: E501

import os
from collections.abc import Generator
from contextlib import contextmanager

import psycopg2
from dotenv import load_dotenv
from icecream import ic
from incolume.academia_jedi import logger

load_dotenv()

DATABASE = os.getenv('DB_DATABASE')
HOST = os.getenv('HOST')
USERSERVER = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASSWORD')
PORT = os.getenv('DB_PORT')
logger.debug(ic(f'{DATABASE=} {HOST=} {USERSERVER=} {PASSWORD=} {PORT=}'))


@contextmanager
def instance_cursor(mode: str = 'r') -> Generator:
    """Cria instancia do cursor.

    O "cursor" é um objeto que permite que você execute comandos SQL no banco de dados e recupere os resultados.
    Ele age como um ponteiro ou um marcador de posição dentro de uma transação ativa no banco de dados.
    O cursor permite que você envie consultas SQL para o banco de dados, recuperar os resultados dessas consultas e, em seguida,
    realizar operações como inserção, atualização e exclusão de dados.
    """
    connection = psycopg2.connect(
        database=DATABASE,
        host=HOST,
        user=USERSERVER,
        password=PASSWORD,
        port=PORT,
    )
    cursor = connection.cursor()
    try:
        yield cursor
    finally:
        if connection and mode in ['r', 'w']:
            if mode == 'w':
                connection.commit()
                logger.debug(ic('Commit realizado com sucesso.'))
            cursor.close()
            connection.close()
            logger.debug(ic('Conexão com PostgreSQL encerrada'))


def cria_db():
    """Cria banco de dados."""
    # establishing the connection
    conn = psycopg2.connect(
        database='postgres',
        user=USERSERVER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
    )
    conn.autocommit = True

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Preparing query to create a database
    sql = f"""CREATE database {DATABASE}
        WITH
        OWNER = {USERSERVER}
        ENCODING = 'utf-8'
    """

    # Creating a database
    cursor.execute(sql)
    ic(f'Database {DATABASE} created successfully..')

    # Closing the connection
    conn.close()


def consulta(user):
    """Consulta usuário."""
    with instance_cursor() as cursor:
        query = """
                SELECT nome, usuario, senha
                FROM REGISTROS
                WHERE usuario = %s
                """
        cursor.execute(query, (user,))
        return cursor.fetchall()


def consulta_geral():
    """Consulta todos os registros."""
    with instance_cursor() as cursor:
        query = """
                SELECT *
                FROM REGISTROS
                """
        cursor.execute(
            query,
        )
        return cursor.fetchall()


def add_registro(nome: str, user: str, senha: str) -> None:
    """Adiciona registros na tabela."""
    connection = psycopg2.connect(
        database=DATABASE,
        host=HOST,
        user=USERSERVER,
        password=PASSWORD,
        port=PORT,
    )
    cursor = connection.cursor()

    query = f"""
        INSERT INTO REGISTROS VALUES
        {nome, user, senha}
        """
    cursor.execute(query)
    connection.commit()
    if connection:
        cursor.close()
        connection.close()
        ic('Conexão com PostgreSQL encerrada')


def cria_tabela():
    """Cria a tabela se não existir."""
    ic(DATABASE)
    ic(HOST)
    ic(USERSERVER)
    ic(PASSWORD)
    ic(PORT)

    connection = psycopg2.connect(
        database=DATABASE,
        host=HOST,
        user=USERSERVER,
        password=PASSWORD,
        port=PORT,
    )
    cursor = connection.cursor()
    ic('AAAAAAA')
    ic(connection)
    query = """
        CREATE TABLE REGISTROS (
            nome varchar(255),
            usuario varchar(255),
            senha varchar(255)
        )
        """
    cursor.execute(query)
    connection.commit()
    ic('Tabela criada')
    if connection:
        cursor.close()
        connection.close()
        ic('Conexão com PostgreSQL encerrada')
