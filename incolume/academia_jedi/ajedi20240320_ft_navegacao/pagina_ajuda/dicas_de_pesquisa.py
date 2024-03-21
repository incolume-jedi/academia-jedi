"""Página de dica."""

import flet as ft


def main(page: ft.Page) -> None:
    """Main."""
    page.title = 'Dicas'

    page.appbar = ft.AppBar(
        title=ft.Text(
            'Dicas',
            weight=ft.FontWeight.BOLD,
            color='white',
        ),
        bgcolor='#3b65ad',
        center_title=True,
        actions=[
            ft.IconButton(ft.icons.MENU, tooltip='Menu', icon_color='black'),
        ],
    )

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(
                icon=ft.icons.CALENDAR_MONTH_ROUNDED,
                label='RESENHA',
            ),
            ft.NavigationDestination(icon=ft.icons.LOUPE, label='BUSCA'),
            ft.NavigationDestination(
                icon=ft.icons.STAR_PURPLE500_OUTLINED,
                label='FAVORITOS',
            ),
            ft.NavigationDestination(icon=ft.icons.HELP, label='AJUDA'),
        ],
        bgcolor='#3b65ad',
    )

    titulo = ft.Text(value='Dicas de Pesquisa', color='#3b65ad', size=60)

    paragraph1 = ft.Text(
        value='Preencha os campos desejados e clique'
        'no botão buscar. Os documentos que possuírem'
        'todos os dados serão retornados.',
        size=30,
    )

    paragraph2 = ft.Text(
        value='Para refinar a pesquisa acrescente aspas'
        'duplas no início e fim do termo pesquisado.'
        'Exemplo: “marco civil da internet”',
        size=30,
    )

    conteudo = ft.Column(
        controls=(
            paragraph1,
            paragraph2,
        ),
        spacing=50,
    )
    page.add(
        titulo,
        conteudo,
    )


ft.app(target=main)
