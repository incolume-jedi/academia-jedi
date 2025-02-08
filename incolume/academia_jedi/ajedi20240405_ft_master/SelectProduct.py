"""Module."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

from Database import ProductsDatabase
from flet import (
    AlertDialog,
    Column,
    DataCell,
    DataColumn,
    DataRow,
    DataTable,
    IconButton,
    ListView,
    MainAxisAlignment,
    Row,
    Text,
    TextButton,
    TextField,
    colors,
    icons,
)

# ruff: noqa: ARG002 A002 DTZ011 C901 T201 ANN201 ERA001 D101 D102 D107 E501 PLR2004


class SelectProduct(AlertDialog):
    def __init__(self, route):
        super().__init__()
        self.route = route
        self.modal = True
        self.title = Row(
            alignment=MainAxisAlignment.CENTER,
            controls=[Text('Lista de Produtos:', width=840)],
        )

        self.tf_find_product = TextField(
            label='Buscar',
            width=840,
            on_change=self.find_product,
        )
        self.dt_products = DataTable(
            expand=True,
            columns=[
                DataColumn(label=Text('ID')),
                DataColumn(label=Text('DESCRIÇÃO')),
                DataColumn(label=Text('MARCA')),
                DataColumn(label=Text('PREÇO')),
                DataColumn(label=Text('SELECIONAR')),
            ],
        )
        self.btn_back = TextButton(text='Voltar', on_click=self.back_clicked)

        self.actions = [
            Column(
                width=840,
                controls=[
                    self.tf_find_product,
                    ListView(
                        height=400,
                        controls=[
                            self.dt_products,
                        ],
                    ),
                    Row(
                        alignment=MainAxisAlignment.END,
                        width=840,
                        controls=[self.btn_back],
                    ),
                ],
            ),
        ]
        self.initialize()

    def build(self):
        return self

    def back_clicked(self, e):
        self.open = False
        self.route.page.update()

    def get_data_from_db(self):
        mydb = ProductsDatabase(self.route)
        mydb.connect()
        result = mydb.select_products()
        mydb.close()
        return result

    def fill_in_table_products(self, fulldata):
        self.dt_products.rows.clear()
        for data in fulldata:
            self.dt_products.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(value=data[0])),
                        DataCell(Text(value=data[1])),
                        DataCell(Text(value=data[3])),
                        DataCell(Text(value=f'R${data[4]}')),
                        DataCell(
                            IconButton(
                                icon=icons.SENSOR_OCCUPIED_ROUNDED,
                                icon_color=colors.PRIMARY,
                                tooltip='Selecionar',
                                data=data[0],
                                on_click=self.select_product,
                            ),
                        ),
                    ],
                ),
            )

    def initialize(self):
        fulldata = self.get_data_from_db()
        self.fill_in_table_products(fulldata)

    def find_product(self, e):
        if self.tf_find_product.value == '':
            self.initialize()
            return

        mydb = ProductsDatabase(self.route)
        mydb.connect()
        result = mydb.find_product(self.tf_find_product.value)
        mydb.close()

        if result:
            self.fill_in_table_products(result)
        else:
            self.dt_products.rows.clear()

        self.route.page.update()

    def select_product(self, e):
        mydb = ProductsDatabase(self.route)
        mydb.connect()
        result = mydb.find_product_by_code(int(e.control.data))
        mydb.close()

        if result:
            self.route.register_sales.load_card(result)
            self.open = False
            self.update()
        else:
            self.route.register_sales.clear_card()

        self.route.register_sales.validate_fields(e)
