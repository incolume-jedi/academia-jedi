"""Module."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

import asyncio

from Database import CustomerDatabase
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
    icons,
)

# ruff: noqa: ARG002 A002 DTZ011 C901 T201 ANN201 ERA001 D101 D102 D107 E501 PLR2004


class SelectCustomer(AlertDialog):
    def __init__(self, route):
        super().__init__()
        self.route = route
        self.modal = True
        self.title = Row(
            expand=True,
            controls=[Text('Selecione o Cliente:', width=600)],
        )

        self.tf_find_customer = TextField(
            label='Buscar...',
            expand=True,
            prefix_icon=icons.SEARCH_OUTLINED,
            on_change=self.find_customer,
        )
        self.btn_back = TextButton(text='Voltar', on_click=self.back_clicked)
        self.dt_customer = DataTable(
            expand=True,
            columns=[
                DataColumn(Text('ID')),
                DataColumn(Text('CLIENTE')),
                DataColumn(Text('CPF')),
                DataColumn(Text('SELEC.')),
            ],
        )

        self.actions = [
            Column(
                width=600,
                expand=True,
                controls=[
                    Row(
                        controls=[
                            self.tf_find_customer,
                        ],
                    ),
                    ListView(
                        height=240,
                        controls=[
                            self.dt_customer,
                        ],
                    ),
                    Row(
                        alignment=MainAxisAlignment.END,
                        controls=[
                            self.btn_back,
                        ],
                    ),
                ],
            ),
        ]
        self.load_table(self.get_customer_data())

    def build(self):
        return self

    def back_clicked(self, e):
        self.data = 'back'
        self.open = False
        self.update()

    def get_customer_data(self):
        mydb = CustomerDatabase(self.route)
        mydb.connect()
        result = mydb.select_customers()
        mydb.close()
        return result

    def load_table(self, fulldata):
        self.dt_customer.rows.clear()
        for data in fulldata:
            self.dt_customer.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(str(data[0]))),
                        DataCell(Text(data[1])),
                        DataCell(Text(data[2])),
                        DataCell(
                            Row([
                                IconButton(
                                    icon=icons.SENSOR_OCCUPIED_OUTLINED,
                                    icon_color='blue',
                                    data=data,
                                    tooltip='Selecionar',
                                    on_click=self.select_customer,
                                ),
                            ]),
                        ),
                    ],
                ),
            )

    def find_customer(self, e):
        if self.tf_find_customer.value == '':
            self.load_table(self.get_customer_data())
            self.update()
            return

        mydb = CustomerDatabase(self.route)
        mydb.connect()
        result = mydb.find_customer(self.tf_find_customer.value)
        mydb.close()
        if result:
            self.load_table(result)
        self.update()

    def select_customer(self, e):
        self.data = e.control.data
        self.open = False
        self.update()

    async def verify_data(self):
        while self.data is None:
            await asyncio.sleep(0.5)
