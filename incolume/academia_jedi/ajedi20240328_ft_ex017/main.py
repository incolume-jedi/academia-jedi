"""Exemplo 17."""

from typing import NoReturn

import flet as ft


def main(page: ft.Page) -> NoReturn:
    """Run it."""

    def pegar_dados(_: ft.ControlEvent) -> NoReturn:
        servidor = entry_servidor.value
        nome_banco = entry_nome_banco.value

        page.add(
            ft.Text(
                value=f'O servidor digitado é {servidor}'
                f' e o banco é {nome_banco}',
            ),
        )

    entry_servidor = ft.TextField(label='Servidor')
    entry_nome_banco = ft.TextField(label='Nome do banco')
    enviar = ft.FilledButton(text='Enviar', on_click=pegar_dados)

    page.add(entry_servidor, entry_nome_banco, enviar)


ft.app(target=main)
