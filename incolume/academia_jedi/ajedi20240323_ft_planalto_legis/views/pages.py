"""Package for pages."""

import flet as ft

from incolume.academia_jedi.ajedi20240323_ft_planalto_legis.views.template import (
    IMAGES,
)
from incolume.academia_jedi.ajedi20240323_ft_planalto_legis.views.styles import (
    text_styles,
)

__author__ = '@britodfbr'  # pragma: no cover


def splash_vw(e: ft.ControlEvent) -> ft.Control:
    """Splash page.
    """
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
    return ft.View()


def resenha_vw(e: ft.ControlEvent) -> ft.Control:
    """Resenha view."""
    return ft.View()


def favoritos_vw(e: ft.ControlEvent) -> ft.Control:
    """Favoritos view."""
    return ft.View()


def busca_vw(e: ft.ControlEvent) -> ft.Control:
    """Busca view."""
    return ft.View()


def ajuda_vw(e: ft.ControlEvent) -> ft.Control:
    """Ajuda view."""
    return ft.View()


def estatutos_vw(e: ft.ControlEvent) -> ft.Control:
    """Estatutos view."""
    return ft.View()


def constituicao_vw(e: ft.ControlEvent) -> ft.Control:
    """Constituição view."""
    return ft.View()


def codigos_vw(e: ft.ControlEvent) -> ft.Control:
    """Codigos view."""
    return ft.View()


def set_navbar(page: ft.Page) -> ft.NavigationBar:
    """Define Navigation Bar."""
    page.update()
    return ft.NavigationBar(
        visible=True,
        # bgcolor=BLUE,
        surface_tint_color=ft.colors.WHITE,
        shadow_color=ft.colors.BLACK87,
        indicator_color=ft.colors.BLUE,
        selected_index=1,
        destinations=[
            ft.NavigationDestination(
                icon=ft.icons.CALENDAR_MONTH_ROUNDED,
                tooltip='Resenha diária',
                label='RESENHA',
            ),
            ft.NavigationDestination(
                icon=ft.icons.SEARCH,
                tooltip='Busca avançada',
                label='BUSCA',
            ),
            ft.NavigationDestination(
                icon=ft.icons.STAR_PURPLE500_OUTLINED,
                tooltip='Atos Favoritos',
                label='FAVORITOS',
            ),
            ft.NavigationDestination(
                icon=ft.icons.HELP,
                label='AJUDA',
            ),
        ],
    )


def page_form(page: ft.Page) -> ft.Container:
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


def page_about(page: ft.Page) -> ft.Container:
    """Page about."""
    page.appbar.title = ft.Text('Sobre')
    return ft.Container(
        margin=10,
        padding=10,
        aspect_ratio=9 / 16,
        content=ft.Column(
            controls=[
                ft.Text(
                    value='Aplicativo desenvolvido para facilitar o acesso'
                    ' à Legislação Federal brasileira. Apresenta toda'
                    ' a base da legislação disponível no Portal da'
                    ' Legislação do Planalto, gerido pelo Centro de'
                    ' Estudos da Subchefia para Assuntos Jurídicos da'
                    ' Secretaria-Geral da Presidência da República.',
                    **text_styles,
                ),
                ft.Text(
                    color='black',
                    text_align=ft.TextAlign.JUSTIFY,
                    size=20,
                    value='Apresenta a pesquisa por Termo (palavra-chave),'
                    ' por ano, por número, por tipo e por situação dos'
                    ' atos. Permite também acesso rápido pelo menu'
                    ' lateral aos principais Códigos, Estatutos e à'
                    ' Constituição.',
                ),
                ft.Text(
                    color='black',
                    text_align=ft.TextAlign.JUSTIFY,
                    size=20,
                    value='Possibilita que o usuário salve os atos de seu'
                    ' interesse na pasta de Favoritos para visualização'
                    ' desse conteúdo também em modo off-line. Essa'
                    ' funcionalidade apresenta um lembrete de '
                    'atualização toda vez que os atos sofrem algum tipo'
                    ' de alteração no seu conteúdo.',
                ),
                ft.Text(
                    color='black',
                    text_align=ft.TextAlign.JUSTIFY,
                    size=20,
                    value='Outra funcionalidade disponibilizada no aplicativo'
                    ' é a Resenha, que traz uma lista com todos os atos'
                    ' publicados naquela data, sempre que houver. É'
                    ' possível também pesquisar por datas específicas'
                    ' para ter acesso às publicações dos atos normativos'
                    ' das datas selecionadas.',
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
    )
