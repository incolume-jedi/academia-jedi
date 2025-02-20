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
    SnackBar,
    Text,
    TextButton,
    TextField,
    colors,
    icons,
)

# ruff: noqa: A002, ANN001, ANN201, ARG002, BLE001, C901, D101, D102, D107, DTZ005, DTZ011, E501, ERA001, N802, N803, N806, PLR2004, S608, T201, TRY300


class Category(AlertDialog):
    def __init__(self, products):
        super().__init__()
        self.products = products
        self.modal = True
        self.title = Row(
            expand=True,
            controls=[Text('Gerenciar Categorias:', width=400)],
        )

        self.tf_new_category = TextField(
            label='Insira a nova categoria',
            dense=True,
            expand=True,
        )
        self.btn_save = IconButton(
            icon=icons.SAVE_OUTLINED,
            icon_color=colors.PRIMARY,
            icon_size=32,
            on_click=self.register_category,
        )
        self.btn_back = TextButton(text='Voltar', on_click=self.back_clicked)
        self.dt_category = DataTable(
            expand=True,
            columns=[
                DataColumn(Text('ID')),
                DataColumn(Text('CATEGORIAS')),
                DataColumn(Text('EXCLUIR')),
            ],
        )

        self.actions = [
            Column(
                width=400,
                expand=True,
                controls=[
                    Row(
                        controls=[
                            self.tf_new_category,
                            self.btn_save,
                        ],
                    ),
                    ListView(
                        height=240,
                        controls=[
                            self.dt_category,
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

    def build(self):
        return self

    def back_clicked(self, e):
        self.products.load_categories()
        self.open = False
        self.update()

    def load_category(self):
        mydb = ProductsDatabase(self.products.route)
        mydb.connect()
        result = mydb.select_category()
        mydb.close()

        self.dt_category.rows.clear()
        for data in result:
            self.dt_category.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(str(data[0]))),
                        DataCell(Text(data[1])),
                        DataCell(
                            Row([
                                IconButton(
                                    icon=icons.DELETE_OUTLINED,
                                    icon_color='red',
                                    data=data[0],
                                    on_click=self.delete_category,
                                ),
                            ]),
                        ),
                    ],
                ),
            )
        self.dt_category.update()

    def register_category(self, e):
        if self.tf_new_category.value.strip() == '':
            return
        mydb = ProductsDatabase(self.products.route)
        mydb.connect()
        result = mydb.register_category(self.tf_new_category.value)
        mydb.close()

        if result == 'success':
            self.page.snack_bar = SnackBar(
                content=Text(
                    'Categoria registrada com sucesso!',
                    color='green',
                ),
            )
        else:
            self.page.snack_bar = SnackBar(
                content=Text(
                    f'Erro ao registrar a categoria: {result}',
                    color='red',
                ),
            )
        self.page.snack_bar.open = True

        self.load_category()

        self.tf_new_category.value = ''
        self.page.update()

    def delete_category(self, e):
        mydb = ProductsDatabase(self.products.route)
        mydb.connect()
        result = mydb.delete_category(e.control.data)
        mydb.close()

        if result == 'success':
            self.page.snack_bar = SnackBar(
                content=Text('Categoria deletada com sucesso!', color='green'),
            )
        else:
            self.page.snack_bar = SnackBar(
                content=Text(
                    f'Erro ao deletar a categoria: {result}',
                    color='red',
                ),
            )
        self.page.snack_bar.open = True

        self.load_category()
        self.page.update()


class Brand(AlertDialog):
    def __init__(self, products):
        super().__init__()
        self.products = products
        self.modal = True
        self.title = Row(
            expand=True,
            controls=[Text('Gerenciar Marcas:', width=400)],
        )

        self.tf_new_brand = TextField(
            label='Insira a nova marca',
            dense=True,
            expand=True,
        )
        self.btn_save = IconButton(
            icon=icons.SAVE_OUTLINED,
            icon_color=colors.PRIMARY,
            icon_size=32,
            on_click=self.register_brand,
        )
        self.btn_back = TextButton(text='Voltar', on_click=self.back_clicked)
        self.dt_brand = DataTable(
            expand=True,
            columns=[
                DataColumn(Text('ID')),
                DataColumn(Text('MARCAS')),
                DataColumn(Text('EXCLUIR')),
            ],
        )

        self.actions = [
            Column(
                width=400,
                expand=True,
                controls=[
                    Row(
                        controls=[
                            self.tf_new_brand,
                            self.btn_save,
                        ],
                    ),
                    ListView(
                        height=240,
                        controls=[
                            self.dt_brand,
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

    def build(self):
        return self

    def back_clicked(self, e):
        self.products.load_brands()
        self.open = False
        self.update()

    def load_brand(self):
        mydb = ProductsDatabase(self.products.route)
        mydb.connect()
        result = mydb.select_brand()
        mydb.close()

        self.dt_brand.rows.clear()
        for data in result:
            self.dt_brand.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(str(data[0]))),
                        DataCell(Text(data[1])),
                        DataCell(
                            Row([
                                IconButton(
                                    icon=icons.DELETE_OUTLINED,
                                    icon_color='red',
                                    data=data[0],
                                    on_click=self.delete_brand,
                                ),
                            ]),
                        ),
                    ],
                ),
            )
        self.dt_brand.update()

    def register_brand(self, e):
        if self.tf_new_brand.value.strip() == '':
            return
        mydb = ProductsDatabase(self.products.route)
        mydb.connect()
        result = mydb.register_brand(self.tf_new_brand.value)
        mydb.close()

        if result == 'success':
            self.page.snack_bar = SnackBar(
                content=Text('Marca registrada com sucesso!', color='green'),
            )
        else:
            self.page.snack_bar = SnackBar(
                content=Text(
                    f'Erro ao registrar a marca: {result}',
                    color='red',
                ),
            )
        self.page.snack_bar.open = True

        self.load_brand()

        self.tf_new_brand.value = ''
        self.page.update()

    def delete_brand(self, e):
        mydb = ProductsDatabase(self.products.route)
        mydb.connect()
        result = mydb.delete_brand(e.control.data)
        mydb.close()

        if result == 'success':
            self.page.snack_bar = SnackBar(
                content=Text('Marca deletada com sucesso!', color='green'),
            )
        else:
            self.page.snack_bar = SnackBar(
                content=Text(
                    f'Erro ao deletar a marca: {result}',
                    color='red',
                ),
            )
        self.page.snack_bar.open = True

        self.load_brand()
        self.page.update()
