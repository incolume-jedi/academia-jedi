
import flet as ft

def main(page: ft.Page):
    def pegar_dados(e):
        servidor = entry_servidor.value
        nome_banco = entry_nome_banco.value

        page.add(ft.Text(value=f'O servidor digitado é {servidor} e o banco é {nome_banco}'))

    entry_servidor = ft.TextField(label='Servidor')
    entry_nome_banco = ft.TextField(label='Nome do banco')
    enviar = ft.FilledButton(text='Enviar', on_click=pegar_dados)

    page.add(entry_servidor, entry_nome_banco, enviar)

ft.app(target=main)
