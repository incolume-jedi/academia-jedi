"""Module."""

__author__ = '@britodfbr'  # pragma: no cover

from typing import NoReturn

import flet as ft
import sqlite3


def main(page: ft.Page) -> NoReturn:
    """Run it."""

    def procurar_no_banco(e):
        nome = e.control.value.strip().lower()

        with sqlite3.connect('./database.db') as db:
            dados = db.execute(
                f'SELECT * FROM funcionarios'
                f" WHERE lower(nome) LIKE '%{nome}%' ",
            )

            dt.rows = [
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(nome)),
                        ft.DataCell(ft.Text(email)),
                    ],
                )
                for nome, email in dados
            ]

            dt.update()

    tf = ft.TextField(on_submit=procurar_no_banco)

    dt = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text('Nome')),
            ft.DataColumn(ft.Text('E-mail')),
        ],
    )

    page.add(tf, dt)


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main)
