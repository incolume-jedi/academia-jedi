"""Página de ajuda."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

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
