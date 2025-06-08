"""Página de ajuda."""

import flet as ft


def main(page: ft.Page) -> None:
    """Main."""
    page.title = 'Perguntas frequentes'

    page.appbar = ft.AppBar(
        title=ft.Text(
            'Perguntas frequentes',
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

    pergunta1 = ft.Text(
        value='1) Portarias de ministros e resoluções'
        ' de órgãos específicos podem ser pesquisados no aplicativo?',
        weight='bold',
        size=30,
    )

    resposta1 = ft.Text(
        value='O aplicativo não disponibiliza portarias ou resoluções'
        ' de órgãos específicos. Para encontrá-los, o usuário deverá'
        ' buscar no sítio eletrônico do ministério, órgão ou ente'
        ' federado responsável pela edição do ato ou, caso se trate'
        ' de ato normativo editado por autoridade do Poder Executivo'
        ' federal, no Diário Oficial da União.',
        size=20,
    )

    pergunta2 = ft.Text(
        value='2) O aplicativo disponibiliza atos normativos'
        ' estaduais ou municipais?',
        weight='bold',
        size=30,
    )

    resposta2 = ft.Text(
        value='O aplicativo disponibiliza apenas atos da legislação federal.'
        ' Para encontrar atos normativos estaduais ou municipais, o usuário'
        ' deverá buscar no sítio eletrônico do ente federado ou nos veículos'
        ' de publicações oficiais.',
        size=20,
    )

    estrutura = ft.Column(
        controls=(
            pergunta1,
            resposta1,
            pergunta2,
            resposta2,
        ),
        spacing=40,
    )

    page.add(estrutura)


ft.app(target=main)
