"""Página de ajuda."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

from logging import info

import flet as ft


def main(page: ft.Page) -> None:
    """Run this app."""
    page.title = 'Ajuda'

    page.scroll = ft.ScrollMode.AUTO

    def route_change(e: ft.ControlEvent) -> None:
        """Route change."""
        page.views.clear()
        page.views.append(
            ft.View(
                '/',
                [
                    ft.AppBar(
                        title=ft.Text(
                            'Ajuda',
                            weight=ft.FontWeight.BOLD,
                            color='white',
                        ),
                        bgcolor='#3b65ad',
                        center_title=True,
                        actions=[
                            ft.IconButton(
                                ft.icons.MENU,
                                tooltip='Menu',
                                icon_color='black',
                            ),
                        ],
                    ),
                    ft.NavigationBar(
                        destinations=[
                            ft.NavigationDestination(
                                icon=ft.icons.CALENDAR_MONTH_ROUNDED,
                                label='RESENHA',
                            ),
                            ft.NavigationDestination(
                                icon=ft.icons.LOUPE,
                                label='BUSCA',
                            ),
                            ft.NavigationDestination(
                                icon=ft.icons.STAR_PURPLE500_OUTLINED,
                                label='FAVORITOS',
                            ),
                            ft.NavigationDestination(
                                icon=ft.icons.HELP,
                                label='AJUDA',
                            ),
                        ],
                        bgcolor='#3b65ad',
                    ),
                    ft.Column(
                        controls=[
                            ft.ResponsiveRow(
                                [
                                    ft.TextButton(
                                        text='Dicas de pesquisa',
                                        style=ft.ButtonStyle(color='#3b65ad'),
                                        on_click=go_dicas,
                                    ),
                                ],
                            ),
                            ft.ResponsiveRow(
                                [
                                    ft.TextButton(
                                        text='Perguntas frequentes',
                                        style=ft.ButtonStyle(color='#3b65ad'),
                                        on_click=go_perguntas,
                                    ),
                                ],
                            ),
                            ft.ResponsiveRow(
                                [
                                    ft.TextButton(
                                        text='Sobre',
                                        style=ft.ButtonStyle(color='#3b65ad'),
                                        on_click=go_sobre,
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )
        if page.route == '/dicas':
            page.views.append(
                ft.View(
                    '/dicas',
                    [
                        ft.AppBar(
                            title=ft.Text(
                                'Dicas',
                                weight=ft.FontWeight.BOLD,
                                color='white',
                            ),
                            bgcolor='#3b65ad',
                            center_title=True,
                            actions=[
                                ft.IconButton(
                                    ft.icons.MENU,
                                    tooltip='Menu',
                                    icon_color='black',
                                ),
                            ],
                        ),
                        ft.NavigationBar(
                            destinations=[
                                ft.NavigationDestination(
                                    icon=ft.icons.CALENDAR_MONTH_ROUNDED,
                                    label='RESENHA',
                                ),
                                ft.NavigationDestination(
                                    icon=ft.icons.LOUPE,
                                    label='BUSCA',
                                ),
                                ft.NavigationDestination(
                                    icon=ft.icons.STAR_PURPLE500_OUTLINED,
                                    label='FAVORITOS',
                                ),
                                ft.NavigationDestination(
                                    icon=ft.icons.HELP,
                                    label='AJUDA',
                                ),
                            ],
                            bgcolor='#3b65ad',
                        ),
                        ft.Column(
                            controls=[
                                ft.Text(
                                    value='Dicas de Pesquisa',
                                    color='#3b65ad',
                                    size=60,
                                ),
                                ft.Text(
                                    value='Preencha os campos desejados'
                                    ' e clique no botão buscar. Os documentos'
                                    ' que possuírem todos os dados serão'
                                    ' retornados.',
                                    size=30,
                                ),
                                ft.Text(
                                    value='Para refinar a pesquisa acrescente'
                                    ' aspas duplas no início e fim do termo'
                                    ' pesquisado.\nExemplo: “marco civil da'
                                    ' internet”',
                                    size=30,
                                ),
                            ],
                            spacing=50,
                        ),
                    ],
                ),
            )
        if page.route == '/perguntas':
            page.views.append(
                ft.View(
                    '/perguntas',
                    [
                        ft.AppBar(
                            title=ft.Text(
                                'Perguntas frequentes',
                                weight=ft.FontWeight.BOLD,
                                color='white',
                            ),
                            bgcolor='#3b65ad',
                            center_title=True,
                            actions=[
                                ft.IconButton(
                                    ft.icons.MENU,
                                    tooltip='Menu',
                                    icon_color='black',
                                ),
                            ],
                        ),
                        ft.NavigationBar(
                            destinations=[
                                ft.NavigationDestination(
                                    icon=ft.icons.CALENDAR_MONTH_ROUNDED,
                                    label='RESENHA',
                                ),
                                ft.NavigationDestination(
                                    icon=ft.icons.LOUPE,
                                    label='BUSCA',
                                ),
                                ft.NavigationDestination(
                                    icon=ft.icons.STAR_PURPLE500_OUTLINED,
                                    label='FAVORITOS',
                                ),
                                ft.NavigationDestination(
                                    icon=ft.icons.HELP,
                                    label='AJUDA',
                                ),
                            ],
                            bgcolor='#3b65ad',
                        ),
                        ft.Column(
                            controls=[
                                ft.Text(
                                    value='1) Portarias de ministros e'
                                    ' resoluções de órgãos específicos podem'
                                    ' ser pesquisados no aplicativo?',
                                    weight='bold',
                                    size=30,
                                ),
                                ft.Text(
                                    value='O aplicativo não disponibiliza'
                                    ' portarias ou resoluções de órgãos'
                                    ' específicos. Para encontrá-los, o'
                                    ' usuário deverá buscar no sítio'
                                    ' eletrônico do ministério, órgão ou ente'
                                    ' federado responsável pela edição do ato'
                                    ' ou, caso se trate de ato normativo'
                                    ' editado por autoridade do Poder'
                                    ' Executivo federal, no Diário Oficial da'
                                    ' União.',
                                    size=20,
                                ),
                                ft.Text(
                                    value='2) O aplicativo disponibiliza atos'
                                    ' normativos estaduais ou municipais?',
                                    weight='bold',
                                    size=30,
                                ),
                                ft.Text(
                                    value='O aplicativo disponibiliza apenas'
                                    ' atos da legislação federal.'
                                    ' Para encontrar atos normativos'
                                    ' estaduais ou municipais, o usuário'
                                    ' deverá buscar no sítio eletrônico do'
                                    ' ente federado ou nos veículos de '
                                    ' publicações oficiais.',
                                    size=20,
                                ),
                            ],
                            spacing=40,
                        ),
                    ],
                ),
            )
        if page.route == '/sobre':
            page.views.append(
                ft.View(
                    '/sobre',
                    [
                        ft.AppBar(
                            title=ft.Text(
                                'Sobre',
                                weight=ft.FontWeight.BOLD,
                                color='white',
                            ),
                            bgcolor='#3b65ad',
                            center_title=True,
                            actions=[
                                ft.IconButton(
                                    ft.icons.MENU,
                                    tooltip='Menu',
                                    icon_color='black',
                                ),
                            ],
                        ),
                        ft.NavigationBar(
                            destinations=[
                                ft.NavigationDestination(
                                    icon=ft.icons.CALENDAR_MONTH_ROUNDED,
                                    label='RESENHA',
                                ),
                                ft.NavigationDestination(
                                    icon=ft.icons.LOUPE,
                                    label='BUSCA',
                                ),
                                ft.NavigationDestination(
                                    icon=ft.icons.STAR_PURPLE500_OUTLINED,
                                    label='FAVORITOS',
                                ),
                                ft.NavigationDestination(
                                    icon=ft.icons.HELP,
                                    label='AJUDA',
                                ),
                            ],
                            bgcolor='#3b65ad',
                        ),
                        ft.Text(
                            value='Aplicativo desenvolvido para facilitar o'
                            ' acesso à Legislação Federal brasileira.'
                            ' Apresenta toda a base da legislação disponível'
                            ' no Portal da Legislação do Planalto, gerido'
                            ' pelo Centro de Estudos da Subchefia para'
                            ' Assuntos Jurídicos da Secretaria-Geral da'
                            ' Presidência da República.\n\nApresenta a'
                            ' pesquisa por Termo (palavra-chave), por ano,'
                            ' por número, por tipo e por situação dos atos.'
                            ' Permite também acesso rápido pelo menu lateral'
                            ' aos principais Códigos, Estatutos e à '
                            ' Constituição.\n\nPossibilita que o usuário'
                            ' salve os atos de seu interesse na pasta de'
                            ' Favoritos para visualização desse conteúdo'
                            ' também em modo off-line. Essa funcionalidade'
                            ' apresenta um lembrete de atualização toda vez'
                            ' que os atos sofrem algum tipo de alteração no'
                            ' seu conteúdo.\n\nOutra funcionalidade'
                            ' disponibilizada no aplicativo é a Resenha, que'
                            ' traz uma lista com todos os atos publicados'
                            ' naquela data, sempre que houver. É possível'
                            ' também pesquisar por datas específicas para ter'
                            ' acesso às publicações dos atos normativos das'
                            ' datas selecionadas. \n\nSão disponibilizados no'
                            ' aplicativo os atos assinados por Presidentes da'
                            ' República – Leis Ordinárias, Leis'
                            ' Complementares, Leis Delegadas, Medidas'
                            ' Provisórias e Decretos.',
                            size=30,
                        ),
                    ],
                ),
            )
        info('%s', e)

    page.update()

    def view_pop(e: ft.ControlEvent) -> None:
        """View Pop."""
        page.views.pop()
        top_view = page.views[-1]
        info('%s', e)
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    def go_dicas(e: ft.ControlEvent) -> None:
        """Go dicas."""
        info('%s', e)
        page.go('/dicas')

    def go_perguntas(e: ft.ControlEvent) -> None:
        """Go perguntas."""
        info('Event: %s', e)
        page.go('/perguntas')

    def go_sobre(e: ft.ControlEvent) -> None:
        """Go sobre."""
        info('%s', e)
        page.go('/sobre')

    page.go(page.route)


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main)
