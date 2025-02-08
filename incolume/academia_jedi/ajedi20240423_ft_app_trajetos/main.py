import sqlite3

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293
import flet as ft
from icecream import ic


# ruff: noqa: F841
class LogApp:
    """Class LogApp."""

    def __init__(self, page: ft.Page):
        """Initializer."""
        self.page = page
        self.page.padding = 10
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.bgcolor = ft.colors.CYAN_50
        self.page.window_width = 410
        self.page.window_height = 650
        self.page.window_resizable = False
        self.page.window_always_on_top = True
        self.city = ''
        self.day = ''
        self.new_city_ = ft.Ref[ft.TextField]()
        self.new_day_ = ft.Ref[ft.Dropdown]()
        self.new_day_2 = ft.Ref[ft.Dropdown]()
        self.observation = ft.Ref[ft.TextField]()
        self.db_execute(
            'CREATE TABLE IF NOT EXISTS register(cidade, dia1, dia2, obs)',
        )
        self.page.title = 'Roteirização Logística'
        self.main_page()

    def db_execute(self, query, params: list | None = None):
        """Db execute."""
        params = params or []
        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            cur.execute(query, params)
            con.commit()
            return cur.fetchall()

    def day_routh_container(self):
        """Day routh container."""
        return ft.Container(
            padding=ft.padding.only(top=20),
            content=ft.Column(
                scroll=ft.ScrollMode.AUTO,
                height=200,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(f'Cidade cadastrada {ct + 1}', size=18)
                    for ct in range(50)
                    # ft.Text(
                    # f'Cidades cadastradas {self.result}', size=18),
                    # ft.Text(
                    # value='Terça-feira', weight=ft.FontWeight.W_700, size=25)
                ],
            ),
        )

    def set_value(self, e):
        """Funcao que colocar os dados em variáveis."""
        self.city = self.new_city_.current.value
        self.day = self.new_day_.current.value
        self.day2 = self.new_day_2.current.value
        self.obs1 = self.observation.current.value
        ic(self.city, self.day, self.day2, self.obs1)
        self.add_bd(c='', d1='', d2='', o1='')

    def add_bd(
        self,
        c,
        d1,
        d2,
        o1,
    ):
        """Funcao que grava os dados coletados no banco."""
        c = self.city.capitalize()
        d1 = self.day
        d2 = self.day2
        o1 = self.obs1

        if c:
            self.db_execute(
                query='insert into register values(?, ?, ?, ?)',
                params=[c, d1, d2, o1],
            )
            self.new_city_.current.value = ''
            self.new_day_.current.value = ''
            self.new_day_2.current.value = ''
            self.observation.current.value = ''
            self.new_city_.current.focus()
            self.page.update()

    def result(self, e):
        """Result."""
        self.e = e.control.value
        self.result = self.db_execute(
            "select * from register where cidade like '%s'" % self.e,
        )
        self.page.update()

    def new_city(self):
        """New city."""
        return ft.Container(
            padding=ft.padding.only(top=20),
            height=self.page.height * 0.5,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    new_city_ := ft.TextField(
                        ref=self.new_city_,
                        hint_text='Nova cidade',
                    ),
                    new_day_ := ft.Dropdown(
                        ref=self.new_day_,
                        label='Selecione o dia da rota',
                        options=[
                            ft.dropdown.Option(text='Domingo'),
                            ft.dropdown.Option(text='Segunda-feira'),
                            ft.dropdown.Option(text='Terca-feira'),
                            ft.dropdown.Option(text='Quarta-feira'),
                            ft.dropdown.Option(text='Quinta-feira'),
                            ft.dropdown.Option(text='Sexta-feira'),
                            ft.dropdown.Option(text='Sabado'),
                        ],
                    ),
                    new_day_2 := ft.Dropdown(
                        ref=self.new_day_2,
                        label='Selecione um segundo dia da rota',
                        options=[
                            ft.dropdown.Option(text='Domingo'),
                            ft.dropdown.Option(text='Segunda-feira'),
                            ft.dropdown.Option(text='Terca-feira'),
                            ft.dropdown.Option(text='Quarta-feira'),
                            ft.dropdown.Option(text='Quinta-feira'),
                            ft.dropdown.Option(text='Sexta-feira'),
                            ft.dropdown.Option(text='Sabado'),
                        ],
                    ),
                    observation := ft.TextField(
                        ref=self.observation,
                        hint_text='Observacao de entrega',
                        min_lines=3,
                        max_lines=5,
                    ),
                    ft.ElevatedButton(
                        text='Cadastrar',
                        on_click=self.set_value,
                    ),
                ],
            ),
        )

    def main_page(self):
        """Main page."""
        show = self.day_routh_container()
        register = self.new_city()
        input_bar = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.TextField(
                    hint_text='Digite a cidade',
                    on_change=self.result,
                ),
                ft.FloatingActionButton(
                    icon=ft.icons.NAVIGATE_NEXT_OUTLINED,
                    on_click=self.result,
                ),
            ],
        )

        tabs = ft.Tabs(
            selected_index=0,
            scrollable=False,
            tabs=[
                ft.Tab(text='Dia da Rota', content=show),
                ft.Tab(text='Cadastrar cidade', content=register),
            ],
        )

        self.page.add(input_bar, tabs)


ft.app(target=LogApp)
