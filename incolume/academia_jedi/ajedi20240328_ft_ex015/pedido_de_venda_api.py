"""Exemplo pedido de vendas."""

from typing import NoReturn

import flet as ft
from icecream import ic

myshape = {
    ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(
        radius=20,
    ),
    ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(
        radius=2,
    ),
}


def main(page: ft.Page) -> NoReturn:
    """Run it."""
    page.theme_mode = 'dark'

    def page_resize(_):
        pw.value = f'{page.width} px'
        pw.update()

    # ======================================================================
    def pick_files_result(e: ft.FilePickerResultEvent) -> NoReturn:
        if e.files:
            file_paths = [
                file.path for file in e.files
            ]  # Extrair caminhos dos arquivos
            selected_files.value = '\n'.join(
                file_paths,
            )  # Exibir caminhos separados por linha
            selected_files.update()
        else:
            selected_files.value = 'Cancelled!'
            selected_files.update()

    def process_file(file_path):
        ic(f'Arquivo selecionado: {file_path}')

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text(col={'md': 12})

    page.overlay.append(pick_files_dialog)

    # =======================================================================

    page.on_resize = page_resize

    pw = ft.Text(bottom=50, right=50, style='displaySmall')
    page.overlay.append(pw)

    page.add(
        ft.ResponsiveRow([
            ft.Container(
                content=ft.ElevatedButton(
                    'Importar Pedido de Planilha',
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=False,
                    ),
                    width=400,
                    style=ft.ButtonStyle(
                        color={
                            ft.MaterialState.HOVERED: ft.colors.WHITE,
                            ft.MaterialState.FOCUSED: ft.colors.BLUE,
                            ft.MaterialState.DEFAULT: ft.colors.BLACK,
                        },
                        bgcolor={
                            ft.MaterialState.FOCUSED: ft.colors.PINK_200,
                            '': ft.colors.BLUE_300,
                        },
                        padding={ft.MaterialState.HOVERED: 20},
                        overlay_color=ft.colors.TRANSPARENT,
                        elevation={'pressed': 0, '': 1},
                        animation_duration=500,
                        side={
                            ft.MaterialState.DEFAULT: ft.BorderSide(
                                1,
                                ft.colors.BLUE,
                            ),
                            ft.MaterialState.HOVERED: ft.BorderSide(
                                2,
                                ft.colors.BLUE,
                            ),
                        },
                        shape=myshape,
                    ),
                ),
                # bgcolor=ft.colors.YELLOW,
                # padding=5,
                width=55,
                height=55,
                col={'md': 12},
            ),
        ]),
        ft.ResponsiveRow([selected_files]),
        ft.ResponsiveRow(
            [
                ft.TextField(label='Código', col={'md': 1}),
                ft.FilledButton(
                    text='Buscar',
                    style=(
                        ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=0),
                        )
                    ),
                    col={'md': 1},
                ),
                ft.TextField(label='Produto Escolhido', col={'md': 9}),
                ft.TextField(label='Quantidade', col={'md': 1}),
            ],
            vertical_alignment=ft.CrossAxisAlignment.STRETCH,
            run_spacing={'xs': 10},
        ),
    )
    # page_resize(None)


ft.app(target=main)
