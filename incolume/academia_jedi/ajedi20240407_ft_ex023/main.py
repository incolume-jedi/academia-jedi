"""Module."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

from typing import NoReturn

import flet as ft

__author__ = '@LineIndent'  # pragma: no cover

# ruff: noqa: FBT001 FBT003

# Define a final class to handle data between controls
# Some dumy data to filll out the table
dummy_data = {
    0: {
        'name': 'Apple',
        'description': 'Red and juicy',
        'quantity': 5,
        'price': 1.99,
    },
    1: {
        'name': 'Bread',
        'description': 'Whole wheat loaf',
        'quantity': 2,
        'price': 3.49,
    },
    2: {
        'name': 'Milk',
        'description': 'Organic whole milk',
        'quantity': 1,
        'price': 2.99,
    },
    3: {
        'name': 'Carrot',
        'description': 'Fresh and crunchy',
        'quantity': 10,
        'price': 0.99,
    },
    4: {
        'name': 'Eggs',
        'description': 'Free-range brown eggs',
        'quantity': 12,
        'price': 2.79,
    },
    5: {
        'name': 'Chicken',
        'description': 'Boneless skinless breasts',
        'quantity': 2,
        'price': 7.99,
    },
    6: {
        'name': 'Banana',
        'description': 'Ripe and yellow',
        'quantity': 6,
        'price': 0.49,
    },
}


class Controller:
    """Controller class."""

    items: dict = dummy_data
    counter: int = len(items)

    @staticmethod
    def get_items():
        """Get item."""
        return Controller.items

    @staticmethod
    def add_item(data: dict) -> NoReturn:
        """Add item."""
        Controller.items[Controller.counter] = data
        Controller.counter += 1


# Define style and attributes for header class
header_style = {
    'height': 60,
    'bgcolor': '#081d33',
    'border_radius': ft.border_radius.only(top_left=15, top_right=15),
    'padding': ft.padding.only(left=15, right=15),
}


def search_field(function: callable) -> ft.TextField:
    """A method that creates and returns a textfield."""
    return ft.TextField(
        border_color='transparent',
        height=20,
        text_size=14,
        content_padding=0,
        cursor_color='white',
        cursor_width=1,
        color='white',
        hint_text='Search',
        on_change=function,
    )


def search_bar(control: ft.TextField) -> ft.Container:
    """A method that adds a container to the search_field."""
    return ft.Container(
        width=350,
        bgcolor='white10',
        border_radius=6,
        opacity=0,
        animate_opacity=300,
        padding=8,
        content=ft.Row(
            spacing=10,
            vertical_alignment='center',
            controls=[
                ft.Icon(
                    name=ft.icons.SEARCH_ROUNDED,
                    size=17,
                    opacity=0.85,
                ),
                control,
            ],
        ),
    )


class Header(ft.Container):
    """Define header class."""

    def __init__(self, dt: ft.DataTable):
        """Init class."""
        super().__init__(**header_style, on_hover=self.toggle_search)
        # create a dt attribute
        self.dt = dt

        # create a textfield for search/filter
        self.search_value = search_field(self.filter_dt_rows)

        # create a searchbox
        self.search = search_bar(self.search_value)

        # define other class attributes
        self.name = ft.Text('Line Indent')
        self.avatar = ft.IconButton('person')

        # compile the attributes inside the header contianer
        self.content = ft.Row(
            alignment='spaceBetween',
            controls=[self.name, self.search, self.avatar],
        )

    def toggle_search(self, e: ft.HoverEvent) -> NoReturn:
        """Define method that toggles search box visibility."""
        self.search.opacity = 1 if e.data == 'true' else 0
        self.search.update()

    def filter_dt_rows(self, e: ft.ControlEvent) -> NoReturn:
        """Define a placeholder method for filtering data."""
        # finally, we can filter the data based on the
        # characters in the search box
        # we need to access th data table instance's rows
        for data_rows in self.dt.rows:
            # I'm only fitlering based on column one
            # so only the first index position [0]
            data_cell = data_rows.cells[0]
            # we change the visibility against whats being
            # typed in the search box.
            # we also handle case sensitivity by setting
            # everything to lower case, i.e, lower()
            data_rows.visible = (
                e.control.value.lower() in data_cell.content.value.lower()
            )

            data_rows.update()


# Define form class styling and attributes
form_style = {
    'border_radius': 8,
    'border': ft.border.all(1, '#ebebeb'),
    'bgcolor': 'white10',
    'padding': 15,
}


def text_field():
    """Define a method that creates and returns a textfield."""
    return ft.TextField(
        border_color='transparent',
        height=20,
        text_size=13,
        content_padding=0,
        cursor_color='black',
        cursor_width=1,
        cursor_height=18,
        color='black',
    )


def text_field_container(
    expand: bool | int,
    name: str,
    control: ft.TextField,
) -> ft.Container:
    """Ext define a container to wrap the textfield in."""
    return ft.Container(
        expand=expand,
        height=45,
        bgcolor='#ebebeb',
        border_radius=6,
        padding=8,
        content=ft.Column(
            spacing=1,
            controls=[
                ft.Text(value=name, size=9, color='black', weight='bold'),
                control,
            ],
        ),
    )


# Next, define a form class
class Form(ft.Container):
    """Form class."""

    def __init__(self, dt: ft.DataTable):
        """Init class."""
        super().__init__(**form_style)
        # create a dt attribute
        self.dt = dt

        # define the 4 row textfields
        self.row1_value = text_field()
        self.row2_value = text_field()
        self.row3_value = text_field()
        self.row4_value = text_field()

        # define and wrap each inside a container
        self.row1 = text_field_container(True, 'Row One', self.row1_value)
        self.row2 = text_field_container(3, 'Row Two', self.row2_value)
        self.row3 = text_field_container(1, 'Row Three', self.row3_value)
        self.row4 = text_field_container(1, 'Row Four', self.row4_value)

        # define a button to submit the data
        self.submit = ft.ElevatedButton(
            text='Submit',
            style=ft.ButtonStyle(
                shape={'': ft.RoundedRectangleBorder(radius=8)},
            ),
            on_click=self.submit_data,
        )

        # compile all the attibutes into the class contianer
        self.content = ft.Column(
            expand=True,
            controls=[
                ft.Row(controls=[self.row1]),
                ft.Row(controls=[self.row2, self.row3, self.row4]),
                ft.Row(controls=[self.submit], alignment='end'),
            ],
        )

    # defie a method to submit data
    def submit_data(self, _: ft.TapEvent) -> NoReturn:
        """We get the value for each textfield.

        and create a data structure for it.
        """
        data = {
            'col1': self.row1_value.value,
            'col2': self.row2_value.value,
            'col3': self.row3_value.value,
            'col4': self.row4_value.value,
        }

        # next, we call the controller and add the data to our items dict
        Controller.add_item(data)

        # finally, clear the entries and re populate the data table
        self.clear_entries()
        self.dt.fill_data_table()

    # define a method to clear entries post-submit
    def clear_entries(self):
        """Clear entries fields."""
        self.row1_value.value = ''
        self.row2_value.value = ''
        self.row3_value.value = ''
        self.row4_value.value = ''

        self.content.update()


# Define some data table style, attributes, and columns
column_names = ['Column One', 'Column Two', 'Column Three', 'Column Four']

data_table_style = {
    'expand': True,
    'border_radius': 8,
    'border': ft.border.all(2, '#ebebeb'),
    'horizontal_lines': ft.border.BorderSide(1, '#ebebeb'),
    'columns': [
        # use list comprehension to create dt columns
        ft.DataColumn(ft.Text(index, size=12, color='black', weight='bold'))
        for index in column_names
    ],
}


# Next, define a class for the data table
class DataTable(ft.DataTable):
    """Personal DataTable."""

    def __init__(self):
        """Init class."""
        super().__init__(**data_table_style)
        # create a attirbute to get items
        self.df = Controller.get_items()

    def fill_data_table(self) -> NoReturn:
        """Clear the data table rows for new/updated batch."""
        self.rows = []
        # check dict data type to understand following loop
        for values in self.df.values():
            # create a new DataRow
            data = ft.DataRow()
            data.cells = [
                ft.DataCell(ft.Text(value, color='black'))
                for value in values.values()
            ]

            self.rows.append(data)

        self.update()


def main(page: ft.Page) -> NoReturn:
    """Run it."""
    page.bgcolor = '#fdfdfd'

    table = DataTable()
    header = Header(dt=table)
    form = Form(dt=table)

    page.add(
        ft.Column(
            expand=True,
            controls=[
                # header ...
                header,
                ft.Divider(height=2, color='transparent'),
                # form ...
                form,
                ft.Column(
                    scroll='hidden',
                    expand=True,
                    controls=[ft.Row(controls=[table])],  # table ...
                ),
            ],
        ),
    )

    page.update()
    # we can fill out the dt after we add the control to the page
    table.fill_data_table()


if __name__ == '__main__':  # pragma: no cover
    ft.app(target=main)
