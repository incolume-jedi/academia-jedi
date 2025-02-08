"""Module."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

from flet import (
    AlertDialog,
    Checkbox,
    Column,
    Divider,
    Dropdown,
    Icon,
    MainAxisAlignment,
    PopupMenuButton,
    PopupMenuItem,
    Radio,
    RadioGroup,
    Row,
    Text,
    TextButton,
    TextField,
    Theme,
    ThemeMode,
    colors,
    dropdown,
    icons,
)

# ruff: noqa: ARG002 A002 DTZ011 C901 T201 ANN201 ERA001 D101 D102 D107 E501 PLR2004


class SetGeneralConfig(AlertDialog):
    def __init__(self, route):
        super().__init__()
        self.route = route
        self.modal = True
        self.title = Row(
            expand=True,
            alignment='center',
            controls=[Text('Configurações', width=700, text_align='center')],
        )

        self.dd_color_theme = Dropdown(
            dense=True,
            expand=True,
            label='Tema',
            value='Claro',
            options=[dropdown.Option('Claro'), dropdown.Option('Escuro')],
            on_change=self.theme_mode_changed,
        )
        self.pmbtn_color_seed = PopupMenuButton(
            icon=icons.COLOR_LENS_OUTLINED,
            tooltip='Trocar cor do tema',
            items=[
                PopupMenuItem(
                    content=Row(
                        controls=[
                            Icon(
                                icons.COLOR_LENS_OUTLINED,
                                color=colors.PURPLE_300,
                            ),
                            Text('Roxo'),
                        ],
                    ),
                    on_click=self.change_color_seed,
                ),
                PopupMenuItem(
                    content=Row(
                        controls=[
                            Icon(
                                icons.COLOR_LENS_OUTLINED,
                                color=colors.ORANGE_300,
                            ),
                            Text('Laranja'),
                        ],
                    ),
                    on_click=self.change_color_seed,
                ),
                PopupMenuItem(
                    content=Row(
                        controls=[
                            Icon(
                                icons.COLOR_LENS_OUTLINED,
                                color=colors.GREEN_300,
                            ),
                            Text('Verde'),
                        ],
                    ),
                    on_click=self.change_color_seed,
                ),
                PopupMenuItem(
                    content=Row(
                        controls=[
                            Icon(
                                icons.COLOR_LENS_OUTLINED,
                                color=colors.RED_300,
                            ),
                            Text('Vermelho'),
                        ],
                    ),
                    on_click=self.change_color_seed,
                ),
                PopupMenuItem(
                    content=Row(
                        controls=[
                            Icon(
                                icons.COLOR_LENS_OUTLINED,
                                color=colors.BLUE_300,
                            ),
                            Text('Azul'),
                        ],
                    ),
                    on_click=self.change_color_seed,
                ),
                PopupMenuItem(
                    content=Row(
                        controls=[
                            Icon(
                                icons.COLOR_LENS_OUTLINED,
                                color=colors.YELLOW_300,
                            ),
                            Text('Amarelo'),
                        ],
                    ),
                    on_click=self.change_color_seed,
                ),
                PopupMenuItem(
                    content=Row(
                        controls=[
                            Icon(
                                icons.COLOR_LENS_OUTLINED,
                                color=colors.INDIGO_300,
                            ),
                            Text('Indigo'),
                        ],
                    ),
                    on_click=self.change_color_seed,
                ),
                PopupMenuItem(
                    content=Row(
                        controls=[
                            Icon(
                                icons.COLOR_LENS_OUTLINED,
                                color=colors.TEAL_300,
                            ),
                            Text('Teal'),
                        ],
                    ),
                    on_click=self.change_color_seed,
                ),
                PopupMenuItem(
                    content=Row(
                        controls=[
                            Icon(
                                icons.COLOR_LENS_OUTLINED,
                                color=colors.LIME_300,
                            ),
                            Text('Lime'),
                        ],
                    ),
                    on_click=self.change_color_seed,
                ),
                PopupMenuItem(
                    content=Row(
                        controls=[
                            Icon(
                                icons.COLOR_LENS_OUTLINED,
                                color=colors.BROWN_400,
                            ),
                            Text('Marrom'),
                        ],
                    ),
                    on_click=self.change_color_seed,
                ),
            ],
        )
        self.extend_menu = Checkbox(
            value=False,
            label='Menu lateral extendido',
            on_change=self.extended_menu_changed,
        )

        self.tf_company_name = TextField(
            label='Nome da Empresa',
            dense=True,
            expand=True,
        )
        self.tf_adress = TextField(label='Endereço', dense=True, expand=4)
        self.tf_tel = TextField(label='Telefone', dense=True, expand=1)
        self.tf_email = TextField(label='Email', dense=True, expand=True)

        self.btn_back = TextButton(text='Voltar', on_click=self.back_clicked)
        self.btn_save = TextButton(
            text='Salvar Configurações',
            tooltip='Salvar configurações como "default"',
        )

        self.actions = [
            Column(
                width=700,
                expand=True,
                controls=[
                    Text(value='Configurações Gerais:'),
                    Row(
                        controls=[
                            self.dd_color_theme,
                            self.pmbtn_color_seed,
                            self.extend_menu,
                        ],
                    ),
                    Divider(height=1, color='transparent'),
                    Text(value='Dados da Empresa:'),
                    Column(
                        controls=[
                            Row(
                                controls=[
                                    self.tf_company_name,
                                    self.tf_email,
                                ],
                            ),
                            Row(
                                controls=[
                                    self.tf_adress,
                                    self.tf_tel,
                                ],
                            ),
                        ],
                    ),
                    Divider(height=1, color='transparent'),
                    Text(value='Filtros de Venda:'),
                    RadioGroup(
                        content=Column(
                            spacing=0,
                            controls=[
                                Radio(
                                    value='today',
                                    label='Exibir vendas do dia',
                                ),
                                Radio(
                                    value='seven',
                                    label='Exibir vendas dos últimos sete dias',
                                ),
                                Radio(
                                    value='thirty',
                                    label='Exibir vendas dos últimos trinta dias',
                                ),
                                Radio(
                                    value='all',
                                    label='Exibir todas as vendas',
                                ),
                            ],
                        ),
                        on_change=self.change_radio_group,
                    ),
                    Row(
                        alignment=MainAxisAlignment.END,
                        controls=[self.btn_back, self.btn_save],
                    ),
                ],
            ),
        ]

    def build(self):
        return self

    def back_clicked(self, e):
        self.open = False
        self.route.page.update()

    def change_color_seed(self, e):
        self.route.page.theme = Theme(
            color_scheme_seed=e.control.content.controls[0].color,
        )
        self.route.page.update()

    def change_radio_group(self, e):
        buttons = {
            'today': self.route.sales.btn_filter_today,
            'seven': self.route.sales.btn_filter_previous_seven,
            'thirty': self.route.sales.btn_filter_previous_thirty,
            'all': self.route.sales.btn_filter_all,
        }

        for key in buttons:
            buttons[key].selected = False
        buttons[e.control.value].selected = True
        if self.route.bar.text_title.value == 'Vendas':
            self.route.sales.fill_in_table_sales()
            self.route.sales.update()

    def theme_mode_changed(self, e):
        if self.dd_color_theme.value == 'Claro':
            self.route.page.theme_mode = ThemeMode.LIGHT
            self.route.bar.btn_change_theme.icon = icons.DARK_MODE_OUTLINED
        else:
            self.route.page.theme_mode = ThemeMode.DARK
            self.route.bar.btn_change_theme.icon = icons.WB_SUNNY_OUTLINED

        self.route.page.update()

    def extended_menu_changed(self, e):
        self.route.menu.nnrail.extended = e.control.value
        self.route.menu.update()
