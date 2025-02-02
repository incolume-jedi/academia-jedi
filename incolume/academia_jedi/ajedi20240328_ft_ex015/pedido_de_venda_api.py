"""Exemplo pedido de vendas."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

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
