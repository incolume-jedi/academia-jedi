"""Module."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

from ConfirmDialog import ConfirmDialog
from Database import ProductsDatabase, SalesDatabase
from flet import (
    Card,
    Column,
    Container,
    CrossAxisAlignment,
    DataCell,
    DataColumn,
    DataRow,
    DataTable,
    Divider,
    FilePickerResultEvent,
    IconButton,
    ListView,
    MainAxisAlignment,
    Row,
    Text,
    TextAlign,
    TextField,
    TextThemeStyle,
    UserControl,
    VerticalDivider,
    colors,
    icons,
)
from Notification import Notification
from Reports import ProductsReport
from Validator import Validator

# ruff: noqa: ARG002 A002 DTZ011 C901 T201 ANN001 ANN201 ERA001 D101 D102 D107 E501 PLR2004 BLE001 DTZ005 N802


class Products(UserControl):
    def __init__(self, route):
        super().__init__()
        self.route = route

        self.tf_find_product = TextField(
            label='Buscar...',
            expand=True,
            dense=True,
            prefix_icon=icons.SEARCH_ROUNDED,
            on_change=self.find_products,
        )
        self.btn_see_low_stock = IconButton(
            icon=icons.INVENTORY_OUTLINED,
            tooltip='Ver produtos com estoque baixo',
            on_click=self.see_low_stock_clicked,
        )
        self.btn_clear_filters = IconButton(
            icon=icons.CLEAR_ALL_OUTLINED,
            tooltip='Limpar Filtros',
            on_click=self.clear_filter_clicked,
        )
        self.btn_print = IconButton(
            icon=icons.PICTURE_AS_PDF_OUTLINED,
            tooltip='Gerar arquivo .pdf',
            on_click=self.pdf_clicked,
        )
        self.btn_new_product = IconButton(
            tooltip='Adicionar Produto',
            icon=icons.ADD_OUTLINED,
            icon_color=colors.PRIMARY,
            icon_size=36,
            on_click=self.new_product_clicked,
        )

        self.dt_products = DataTable(
            expand=True,
            divider_thickness=0.4,
            # heading_row_color=colors.ON_INVERSE_SURFACE,
            columns=[
                DataColumn(Text('ID')),
                DataColumn(Text('DESCRIÇÃO')),
                DataColumn(Text('MARCA')),
                DataColumn(Text('PREÇO')),
                DataColumn(Text('AÇÕES')),
            ],
        )

        self.dt_order_history = DataTable(
            column_spacing=15,
            divider_thickness=0.4,
            # heading_row_color=colors.ON_INVERSE_SURFACE,
            expand=True,
            columns=[
                DataColumn(Text('Pedido')),
                DataColumn(Text('Data')),
                DataColumn(Text('Valor')),
                DataColumn(Text('Ver')),
            ],
        )
        self.text_total = Text(
            value='R$0,00',
            style=TextThemeStyle.TITLE_MEDIUM,
        )

        self.side_card_column = Column()
        self.side_card = Card(
            elevation=1.5,
            animate_scale=200,
            # expand=True,
            surface_tint_color=colors.INVERSE_PRIMARY,
            content=Container(
                padding=10,
                content=self.side_card_column,
            ),
        )

    def build(self):
        page_content = Container(
            # bgcolor='red',
            padding=0,
            border_radius=5,
            expand=True,
            content=Column(
                controls=[
                    # Corpo principal
                    Container(
                        # bgcolor='white',
                        expand=True,
                        content=Row(
                            vertical_alignment=CrossAxisAlignment.START,
                            controls=[
                                Container(
                                    # bgcolor='red',
                                    expand=5,
                                    border_radius=5,
                                    padding=15,
                                    content=Column(
                                        spacing=25,
                                        controls=[
                                            Row(
                                                spacing=20,
                                                controls=[
                                                    self.btn_see_low_stock,
                                                    self.btn_clear_filters,
                                                    self.btn_print,
                                                    self.tf_find_product,
                                                    self.btn_new_product,
                                                ],
                                            ),
                                            ListView(
                                                expand=True,
                                                controls=[
                                                    self.dt_products,
                                                ],
                                            ),
                                        ],
                                    ),
                                ),
                                VerticalDivider(width=1),
                                Container(
                                    # bgcolor='red',
                                    expand=2,
                                    border_radius=5,
                                    padding=15,
                                    content=Column(
                                        alignment=MainAxisAlignment.START,
                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                        spacing=20,
                                        controls=[
                                            Column(
                                                # expand=1,
                                                horizontal_alignment='center',
                                                controls=[
                                                    self.side_card,
                                                ],
                                            ),
                                            Divider(
                                                height=3,
                                                color='transparent',
                                            ),
                                            Column(
                                                alignment=MainAxisAlignment.START,
                                                horizontal_alignment=CrossAxisAlignment.CENTER,
                                                spacing=10,
                                                expand=True,
                                                controls=[
                                                    Text(
                                                        value='Histórico de Vendas',
                                                        style=TextThemeStyle.TITLE_MEDIUM,
                                                    ),
                                                    ListView(
                                                        expand=True,
                                                        controls=[
                                                            self.dt_order_history,
                                                        ],
                                                    ),
                                                    Row(
                                                        alignment=MainAxisAlignment.END,
                                                        controls=[
                                                            Text(
                                                                'Total:',
                                                                style=TextThemeStyle.TITLE_MEDIUM,
                                                            ),
                                                            self.text_total,
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        )

        return Row(
            expand=True,
            spacing=10,
            controls=[
                page_content,
            ],
        )

    def initialize(self):
        print('Initializing Products Page')
        self.tf_find_product.value = ''
        self.tf_find_product.update()
        self.dt_order_history.rows.clear()
        self.side_card.visible = False
        self.text_total.value = ''
        self.update()
        self.route.page.update()
        self.fill_in_table_products()

    def new_product_clicked(self, e):
        self.route.page.go('/register_product')
        self.route.bar.set_title('Cadastrar Novo Produto')
        self.route.page.update()

    def fill_in_table_products(self, data=None):
        if data is None:
            mydb = ProductsDatabase(self.route)
            mydb.connect()
            result = mydb.select_products()
            mydb.close()
        else:
            result = data

        self.dt_products.rows.clear()
        for data in result:
            self.dt_products.rows.append(
                DataRow(
                    color='error, 0.2' if data[5] <= data[6] else None,
                    cells=[
                        DataCell(Text(str(data[0]))),
                        DataCell(Text(data[1])),
                        DataCell(Text(data[3])),
                        DataCell(
                            TextField(
                                expand=True,
                                value=f'R${data[4]}',
                                border='none',
                                read_only=True,
                                text_align=TextAlign.END,
                            ),
                        ),
                        DataCell(
                            Row(
                                controls=[
                                    IconButton(
                                        icon=icons.EDIT_OUTLINED,
                                        icon_color='blue',
                                        data=data[0],
                                        on_click=self.edit_clicked,
                                    ),
                                    IconButton(
                                        icon=icons.DELETE_OUTLINED,
                                        icon_color='red',
                                        data=data[0],
                                        on_click=self.delete_clicked,
                                    ),
                                ],
                            ),
                        ),
                    ],
                    on_select_changed=lambda e: self.table_row_clicked(
                        e.control.cells[0].content.value,
                    ),
                ),
            )
        self.dt_products.update()

    def edit_clicked(self, e):
        self.route.bar.set_title('Editar Produto')
        self.route.page.go('/register_product')
        self.route.page.update()

        self.route.register_product.text_label.value = 'Editar Produto:'
        self.route.register_product.load_product(e.control.data)

        self.route.register_product.get_sold_from_db()

    def delete_clicked(self, e):
        question = ConfirmDialog(
            self.delete_product,
            'Por favor, confirme:',
            'Tem certeza que deseja excluir o produto?',
        )
        question.data = e.control.data
        self.route.page.dialog = question
        question.open = True
        self.route.page.update()

    def delete_product(self, id):
        mydb = ProductsDatabase(self.route)
        mydb.connect()
        result = mydb.delete_products(id)
        mydb.close()

        if result == 'success':
            Notification(
                self.route.page,
                'Produto excluído com sucesso!',
                'green',
            ).show_message()
            self.fill_in_table_products()
        else:
            Notification(
                self.route.page,
                f'Erro ao excluir o produto: {result}',
                'red',
            ).show_message()

    def find_products(self, e):
        if self.tf_find_product.value == '':
            self.fill_in_table_products()
            return

        mydb = ProductsDatabase(self.route)
        mydb.connect()
        result = mydb.find_product(self.tf_find_product.value)
        mydb.close()

        self.dt_products.rows.clear()
        for data in result:
            self.dt_products.rows.append(
                DataRow(
                    color='error, 0.2' if data[5] <= data[6] else None,
                    cells=[
                        DataCell(Text(str(data[0]))),
                        DataCell(Text(data[1])),
                        DataCell(Text(data[3])),
                        DataCell(
                            TextField(
                                expand=True,
                                value=f'R${data[4]}',
                                border='none',
                                read_only=True,
                                text_align=TextAlign.END,
                            ),
                        ),
                        DataCell(
                            Row(
                                spacing=0,
                                controls=[
                                    IconButton(
                                        icon=icons.EDIT_OUTLINED,
                                        icon_color='blue',
                                        data=data[0],
                                        on_click=self.edit_clicked,
                                    ),
                                    IconButton(
                                        icon=icons.DELETE_OUTLINED,
                                        icon_color='red',
                                        data=data[0],
                                        on_click=self.delete_clicked,
                                    ),
                                ],
                            ),
                        ),
                    ],
                    on_select_changed=lambda e: self.table_row_clicked(
                        e.control.cells[0].content.value,
                    ),
                ),
            )
        self.dt_products.update()

    def create_report_products(self, e: FilePickerResultEvent):
        if e.path is None:
            return
        filename = f'{e.path}.{e.control.allowed_extensions[0]}'
        text = [
            self.dt_products.columns[0].label.value,
            self.dt_products.columns[1].label.value,
            self.dt_products.columns[2].label.value,
            self.dt_products.columns[3].label.value,
        ]

        data = [text]
        for row in range(len(self.dt_products.rows)):
            text = []
            for col in range(len(self.dt_products.columns)):
                text.append(
                    self.dt_products.rows[row].cells[col].content.value,
                ) if col < 4 else None
            data.append(text)

        printer = ProductsReport(
            filename,
            data,
            'Lista de Produtos Cadastrados',
        )
        result, error = printer.print_report()

        if result == 'success':
            Notification(
                self.page,
                f'Arquivo "{filename}" gerado com sucesso!',
                'green',
            ).show_message()
        else:
            Notification(
                self.page,
                f'Erro ao gerar o arquivo {filename}: "{error}"',
                'red',
            ).show_message()

    def pdf_clicked(self, e):
        self.route.save_file_dialog.on_result = self.create_report_products
        self.route.save_file_dialog.save_file(
            dialog_title='Salvar como ...',
            allowed_extensions=['pdf'],
        )
        self.update()

    def table_row_clicked(self, id_product):
        mydb = ProductsDatabase(self.route)
        mydb.connect()
        result = mydb.select_products_full(id_product)
        mydb.close()
        self.fill_in_side_card(result)

        mydb = SalesDatabase(self.route)
        mydb.connect()
        result = mydb.select_sold_history(id_product)
        mydb.close()

        total = sum(x[2] for x in result)
        self.text_total.value = f'R${Validator.format_to_currency(total)}'
        self.update()
        self.fill_in_history_table(result)

    def fill_in_history_table(self, fulldata):
        self.dt_order_history.rows.clear()
        for data in fulldata:
            self.dt_order_history.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(data[0])),
                        DataCell(Text(data[1])),
                        DataCell(
                            Text(
                                value=f'R${Validator.format_to_currency(data[2])}',
                            ),
                        ),
                        DataCell(
                            IconButton(
                                icon=icons.VISIBILITY_OUTLINED,
                                icon_color='blue',
                                tooltip='Ver pedido',
                                data=data[0],
                                on_click=self.see_sale_clicked,
                            ),
                        ),
                    ],
                ),
            )
        self.dt_order_history.update()

    def see_sale_clicked(self, e):
        self.route.page.go('/sales')
        self.route.bar.set_title('Vendas')
        self.route.menu.nnrail.selected_index = 4
        self.route.menu.update()
        self.route.page.update()

        self.route.sales.select_sale_clicked(e.control.data)

    def get_low_stock(self):
        mydb = ProductsDatabase(self.route)
        mydb.connect()
        result = mydb.select_low_stock()
        mydb.close()
        return result

    def see_low_stock_clicked(self, e):
        result = self.get_low_stock()
        self.fill_in_table_products(result)

    def clear_filter_clicked(self, e):
        self.tf_find_product.value = ''
        self.fill_in_table_products()
        self.update()

    def fill_in_side_card(self, products_data):
        self.side_card.visible = True
        self.side_card_column.controls.clear()
        self.side_card_column.controls.append(
            Row(
                alignment='center',
                controls=[
                    Text(
                        value=f'ID {products_data[0]} - {products_data[1]}',
                        text_align='center',
                        expand=True,
                        style=TextThemeStyle.TITLE_SMALL,
                    ),
                ],
            ),
        )
        self.side_card_column.controls.append(
            Row(
                alignment='left',
                spacing=20,
                controls=[
                    Text(value=f'Cat.: {products_data[2]}'),
                    Text(value=f'Marca: {products_data[3]}'),
                ],
            ),
        )
        self.side_card_column.controls.append(
            Row(
                alignment='left',
                spacing=15,
                controls=[
                    Text(value=f'Est.: {products_data[4]}'),
                    Text(value=f'Est. Min: {products_data[5]}'),
                    Text(value=f'Est. Max: {products_data[6]}'),
                ],
            ),
        )
        self.side_card_column.controls.append(Divider(height=1))
        self.side_card_column.controls.append(
            Text(
                value=f'Custo: R${Validator.format_to_currency(float(products_data[8]))}',
            ),
        )
        self.side_card_column.controls.append(
            Text(
                value=f'Venda: R${Validator.format_to_currency(float(products_data[9]))}',
            ),
        )
        self.side_card_column.controls.append(
            Text(
                value=f'Margem: {Validator.format_to_currency(float(products_data[10]))}%',
            ),
        )
        self.side_card_column.controls.append(Divider(height=1))
        self.side_card_column.controls.append(
            Text(value=f'Observ.: {products_data[7]}'),
        )
        self.side_card_column.update()
