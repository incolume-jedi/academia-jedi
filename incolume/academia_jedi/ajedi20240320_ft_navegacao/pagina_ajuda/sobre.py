"""Página de ajuda."""

import flet as ft


def main(page: ft.Page) -> None:
    """Main."""
    page.title = 'Sobre'

    page.appbar = ft.AppBar(
        title=ft.Text(
            'Sobre',
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

    content = ft.Text(
        value='Aplicativo desenvolvido para facilitar o acesso à Legislação'
        ' Federal brasileira. Apresenta toda a base da legislação disponível'
        ' no Portal da Legislação do Planalto, gerido pelo Centro de Estudos'
        ' da Subchefia para Assuntos Jurídicos da Secretaria-Geral da'
        ' Presidência da República.\n\nApresenta a pesquisa por Termo'
        ' (palavra-chave), por ano, por número, por tipo e por situação dos'
        ' atos. Permite também acesso rápido pelo menu lateral aos principais'
        ' Códigos, Estatutos e à Constituição.\n\nPossibilita que o usuário'
        ' salve os atos de seu interesse na pasta de Favoritos para'
        ' visualização desse conteúdo também em modo off-line. Essa'
        ' funcionalidade apresenta um lembrete de atualização toda vez que os'
        ' atos sofrem algum tipo de alteração no seu conteúdo.\n\nOutra'
        ' funcionalidade disponibilizada no aplicativo é a Resenha, que traz'
        ' uma lista com todos os atos publicados naquela data, sempre que'
        ' houver. É possível também pesquisar por datas específicas para ter'
        ' acesso às publicações dos atos normativos das datas selecionadas.'
        '\n\nSão disponibilizados no aplicativo os atos assinados por'
        ' Presidentes da República – Leis Ordinárias, Leis Complementares,'
        ' Leis Delegadas, Medidas Provisórias e Decretos.',
        size=20,
    )

    page.add(content)


ft.app(target=main)
