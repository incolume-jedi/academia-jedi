"""Exemplo 16."""

from typing import NoReturn

import flet as ft


def main(page: ft.Page) -> NoReturn:
    """Run it."""
    page.add(
        ft.DataTable(
            columns=[
                ft.DataColumn(
                    label=ft.Container(
                        width=200,
                        content=ft.Text('Coluna com tamanho de 200px'),
                    ),
                ),
                ft.DataColumn(
                    label=ft.Container(
                        width=200,
                        content=ft.Text('Coluna com tamanho de 200px'),
                    ),
                ),
                ft.DataColumn(
                    label=ft.Container(
                        width=200,
                        content=ft.Text('Coluna com tamanho de 200px'),
                    ),
                ),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(content=ft.Text(value='Conteúdo...'))
                        for _ in range(3)
                    ],
                )
                for _ in range(10)
            ],
        ),
    )


ft.app(target=main)
