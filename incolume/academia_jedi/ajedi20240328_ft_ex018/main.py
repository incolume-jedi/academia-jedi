
import flet as ft


def main(page: ft.page):
    def criar_db(e):
        servidor = entry_servidor.value
        nome_banco = entry_nome_banco.value
        print(f'O servidor digitado é {servidor} e o banco é {nome_banco}')

    # Estilo dos Buttons
    style = ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=10)
    )

    entry_servidor = ft.TextField(
        label='Servidor', 
        border="underline", 
        hint_text="Qual IP ou nome do Server"
    )
    
    entry_nome_banco = ft.TextField(
        label='Nome do banco', 
        border="underline", 
        hint_text="Qual o nome do DB ?"
    )

    t4 = ft.Column([
        ft.Row([
            entry_servidor,
            ft.ElevatedButton(
                text="Execute",
                width=140,
                height=35,
                style=style,
                on_click=criar_db
            ),
        ]),
    ])

    t6 = ft.Column([
        ft.Row([
            entry_nome_banco,
            ft.ElevatedButton(
                text="Arquivo .bak",
                width=140,
                height=35,
                style=style
            ),
        ]),
    ])

    page.add(t4, t6)


# Definir o diretorio padrao que vai esta as fontes images e icons etc
ft.app(target=main, assets_dir='assets')
