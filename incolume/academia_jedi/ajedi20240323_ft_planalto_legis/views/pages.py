"""Package for pages."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

import flet as ft
from incolume.academia_jedi.ajedi20240323_ft_planalto_legis.views.components import (
    set_appbar,
    set_bg,
    set_navbar,
)
from incolume.academia_jedi.ajedi20240323_ft_planalto_legis.views.styles import (
    text_style1,
)
from incolume.academia_jedi.ajedi20240323_ft_planalto_legis.views.template import (
    IMAGES,
)

__author__ = '@britodfbr'  # pragma: no cover


def not_found_vw(_: ft.ControlEvent) -> ft.Control:
    """Splash page."""
    return ft.View(
        route='/notfound',
        auto_scroll=True,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text(aspect_ratio=9 / 16, opacity=1, value='Não encontrado...'),
        ],
    )


def splash_vw(_: ft.ControlEvent) -> ft.Control:
    """Splash page."""
    return ft.View(
        route='/',
        controls=[
            ft.Image(
                src=IMAGES[0].as_posix(),
                aspect_ratio=9 / 16,
                fit=ft.ImageFit.COVER,
                opacity=1,
            ),
        ],
    )


def home_vw(e: ft.ControlEvent) -> ft.Control:
    """Home view."""
    page = e.page
    return ft.View(
        route='/',
        padding=0,
        appbar=set_appbar(page),
        navigation_bar=set_navbar(page),
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        controls=[set_bg(page)],
    )


def resenha_vw(e: ft.ControlEvent) -> ft.Control:
    """Resenha view."""
    page = e.page
    navbar = set_navbar(page)
    navbar.selected_index = 0
    return ft.View(
        route='/resenha',
        appbar=set_appbar(page, title='resenha'),
        navigation_bar=navbar,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
    )


def favoritos_vw(e: ft.ControlEvent) -> ft.Control:
    """Favoritos view."""
    page = e.page
    navbar = set_navbar(page)
    navbar.selected_index = 2
    return ft.View(
        route='/favoritos',
        appbar=set_appbar(page, title='favoritos'),
        navigation_bar=navbar,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
    )


def busca_vw(e: ft.ControlEvent) -> ft.Control:
    """Busca view."""
    page = e.page
    navbar = set_navbar(page)
    navbar.selected_index = 1
    return ft.View(
        route='/busca',
        appbar=set_appbar(page, title='Busca Avançada'),
        navigation_bar=navbar,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
    )


def ajuda_vw(e: ft.ControlEvent) -> ft.Control:
    """Ajuda view."""
    page = e.page
    navbar = set_navbar(page)
    navbar.selected_index = 3
    return ft.View(
        route='/ajuda',
        appbar=set_appbar(e.page, title='ajuda'),
        navigation_bar=navbar,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Text('Help page...'),
            ft.ElevatedButton(
                text='HOME',
                on_click=lambda _: page.go('/'),
            ),
        ],
    )


def estatutos_vw(e: ft.ControlEvent) -> ft.Control:
    """Estatutos view."""
    return ft.View(
        route='/estatutos',
        appbar=set_appbar(e.page, title='estatutos'),
        navigation_bar=set_navbar(e.page),
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
    )


def constituicao_vw(e: ft.ControlEvent) -> ft.Control:
    """Constituição view."""
    return ft.View(
        route='/constituicao',
        appbar=set_appbar(e.page, title='constituição'),
        navigation_bar=set_navbar(e.page),
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
    )


def codigos_vw(e: ft.ControlEvent) -> ft.Control:
    """Codigos view."""
    return ft.View(
        route='/codigos',
        appbar=set_appbar(e.page, title='códigos'),
        navigation_bar=set_navbar(e.page),
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
    )


def page_form(_: ft.Page) -> ft.Container:
    """Page form."""
    return ft.Container(
        padding=10,
        content=ft.Column(
            [
                ft.TextField(label='Termo'),
                ft.ResponsiveRow(
                    columns=4,
                    controls=[
                        ft.TextField(label='Ano', col=2),
                        ft.TextField(label='Número', col=2),
                    ],
                ),
                ft.Dropdown(
                    width='max',
                    label='Tipo',
                    options=[
                        ft.dropdown.Option('CONSTITUIÇÃO'),
                        ft.dropdown.Option('DECRETO'),
                        ft.dropdown.Option('DECRETO EXECUTIVO'),
                        ft.dropdown.Option('DECRETO NÃO NUMERADO'),
                        ft.dropdown.Option('DECRETO-LEI'),
                        ft.dropdown.Option('EMENDA CONSTITUCIONAL'),
                        ft.dropdown.Option('LEI'),
                        ft.dropdown.Option('LEI COMPLEMENTAR'),
                        ft.dropdown.Option('LEI ORDINÁRIA'),
                        ft.dropdown.Option('MEDIDA PROVISÓRIA'),
                        ft.dropdown.Option('RESOLUÇÃO'),
                    ],
                ),
                ft.Dropdown(
                    width='max',
                    label='Situação',
                    options=[
                        ft.dropdown.Option('NÃO CONSTA REVOGAÇÃO EXPRESSA'),
                        ft.dropdown.Option('REVOGADO'),
                    ],
                ),
                ft.ElevatedButton(
                    text='BUSCAR',
                    icon=ft.icons.SEARCH,
                ),
            ],
        ),
    )


def sobre_vw(_: ft.RouteChangeEvent) -> ft.Control:
    """Page about."""
    return ft.View(
        route='/sobre',
        controls=[
            ft.Container(
                margin=10,
                padding=10,
                aspect_ratio=9 / 16,
                content=ft.Column(
                    controls=[
                        ft.Text(
                            value='Aplicativo desenvolvido para '
                            'facilitar o acesso'
                            ' à Legislação Federal brasileira. Apresenta toda'
                            ' a base da legislação disponível no Portal da'
                            ' Legislação do Planalto, gerido pelo Centro de'
                            ' Estudos da Subchefia para Assuntos Jurídicos da'
                            ' Secretaria-Geral da Presidência da República.',
                            **text_style1,
                        ),
                        ft.Text(
                            color='black',
                            text_align=ft.TextAlign.JUSTIFY,
                            size=20,
                            value='Apresenta a pesquisa por '
                            'Termo (palavra-chave),'
                            ' por ano, por número, por tipo e por situação dos'
                            ' atos. Permite também acesso rápido pelo menu'
                            ' lateral aos principais Códigos, Estatutos e à'
                            ' Constituição.',
                        ),
                        ft.Text(
                            color='black',
                            text_align=ft.TextAlign.JUSTIFY,
                            size=20,
                            value='Possibilita que o usuário '
                            'salve os atos de seu'
                            ' interesse na pasta de Favoritos'
                            ' para visualização'
                            ' desse conteúdo também em modo off-line. Essa'
                            ' funcionalidade apresenta um lembrete de '
                            'atualização toda vez que os atos'
                            ' sofrem algum tipo'
                            ' de alteração no seu conteúdo.',
                        ),
                        ft.Text(
                            color='black',
                            text_align=ft.TextAlign.JUSTIFY,
                            size=20,
                            value=(
                                'Outra funcionalidade disponibilizada'
                                ' no aplicativo é a Resenha, que traz uma'
                                ' lista com todos os atos publicados naquela'
                                ' data, sempre que houver. É possível também'
                                ' pesquisar por datas específicas para ter'
                                ' acesso às publicações dos atos normativos'
                                ' das datas selecionadas.'
                            ),
                        ),
                        ft.Text(
                            color='black',
                            text_align=ft.TextAlign.JUSTIFY,
                            size=20,
                            value='São disponibilizados no aplicativo os atos'
                            ' assinados por Presidentes da República - Leis'
                            ' Ordinárias, Leis Complementares, Leis Delegadas,'
                            ' Medidas Provisórias e Decretos.',
                        ),
                    ],
                ),
            ),
        ],
    )
