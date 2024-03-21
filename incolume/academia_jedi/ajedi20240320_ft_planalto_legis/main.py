"""Main module."""

import flet as ft
from pathlib import Path
from time import sleep
from template import BLUE, IMAGES
import logging

assets = Path(__file__).parent / 'assets'
assert assets.exists(), f'Ops: {assets=}'  # noqa: S101
logging.debug(assets)


def settings_page(page: ft.Page, *, title: str = '') -> ft.Page:
    """Setting page."""
    page.window_always_on_top = True
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.title = title or 'Planalto Legis'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_min_width = 450
    page.window_min_height = 720
    page.padding = 0
    page.window_width = page.window_min_width
    page.window_height = page.window_min_height
    page.scroll = ft.ScrollMode.ALWAYS
    page.window_bgcolor = ft.colors.BLACK
    return page


def set_bg(page: ft.Page) -> ft.Stack:
    """Define background."""
    return ft.Stack(
        scale=1,
        aspect_ratio=9 / 16,
        width=page.window_width,
        height=page.window_height - page.appbar.toolbar_height,
        controls=[
            ft.Image(
                src=IMAGES[1].as_posix(),
                aspect_ratio=9 / 16,
                width=page.window_width,
                height=page.window_height,
                fit=ft.ImageFit.COVER,
                opacity=1,
            ),
            ft.Row(
                controls=[
                    ft.Text(
                        'Image title',
                        color=ft.colors.AMBER,
                        size=40,
                        weight='bold',
                        opacity=0.5,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
    )


def set_appbar(page: ft.Page, logo: str = '', title: str = '') -> ft.AppBar:
    """Define AppBar."""
    logo = logo or Path('images', 'icons', 'icon-nobg-1024.png').as_posix()
    title = title or 'Planalto Legis'
    return ft.AppBar(
        bgcolor=BLUE,
        color=ft.colors.WHITE,
        leading=ft.Image(
            src=logo,
        ),
        leading_width=40,
        toolbar_height=page.window_height * 0.1,
        title=ft.Text(title, weight=ft.FontWeight.W_500),
        center_title=True,
        actions=[
            ft.PopupMenuButton(
                visible=True,
                icon=ft.icons.MENU,
                items=[
                    ft.PopupMenuItem(),
                    ft.Divider(),
                    ft.PopupMenuItem(
                        text='Busca Avançada',
                        on_click=lambda _: logging.debug('busca avançada'),
                    ),
                    ft.PopupMenuItem(
                        text='Constituição',
                        on_click=lambda _: logging.debug('constituição'),
                    ),
                    ft.PopupMenuItem(
                        text='Códigos',
                        on_click=lambda _: logging.debug('códigos'),
                    ),
                    ft.PopupMenuItem(
                        text='Estatutos',
                        on_click=lambda _: logging.debug('estatutos'),
                    ),
                    ft.PopupMenuItem(
                        text='Favoritos',
                        on_click=lambda _: logging.debug('favoritos'),
                    ),
                    ft.PopupMenuItem(
                        text='Resenha',
                        on_click=lambda _: logging.debug('resenha'),
                    ),
                    ft.PopupMenuItem(
                        text='Ajuda',
                        on_click=lambda _: logging.debug('ajuda'),
                    ),
                ],
            ),
        ],
    )


def set_navbar(page: ft.Page) -> ft.NavigationBar:
    """Define Navigation Bar."""
    page.update()
    return ft.NavigationBar(
        visible=True,
        bgcolor=BLUE,
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


text_styles = {
    'size': 20,
    'color': 'black',
    'text_align': ft.TextAlign.JUSTIFY,
    # 'weight': ft.FontWeight.W_900,
}


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


def main(page: ft.Page) -> None:
    """Main proccess."""
    page = settings_page(page)
    page.add(
        ft.Image(
            src=IMAGES[0].as_posix(),
            aspect_ratio=9 / 16,
            fit=ft.ImageFit.COVER,
            opacity=1,
        ),
    )
    logging.debug(page.controls)
    sleep(3.5)
    page.controls.clear()
    page.appbar = set_appbar(page)
    page.navigation_bar = set_navbar(page)
    background = set_bg(page)
    page.add(background)

    sleep(2)
    page.appbar.title = ft.Text('Ops')
    background.controls[1].controls[0].value = 'Ops!!'
    logging.debug(background.controls[1].controls[0])
    page.update()

    sleep(2)
    background.controls.pop(-1)
    background.controls.append(page_about(page))
    page.update()

    sleep(2)
    page.appbar.title = ft.Text('Busca Avançada')
    background.controls.pop(-1)
    background.controls.append(page_form(page))
    page.update()


if __name__ == '__main__':
    ft.app(target=main, assets_dir=assets.as_posix())
