"""Module."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

from Appbar import Appbar
from Config import Config
from Customers import Customers
from flet import Container, FilePicker, Page, Row, VerticalDivider
from Home import Home
from Login import Login
from Products import Products
from RegisterCustomer import RegisterCustomer
from RegisterProducts import RegisterProducts
from RegisterSales import RegisterSales
from Sales import Sales
from SideMenu import SideMenu
from Users import Users

# ruff: noqa: ARG002 A002 DTZ011 C901 T201 ANN001 ANN201 ERA001 D101 D102 D107 E501 PLR2004 BLE001 DTZ005 N802


class InfostoreApp:
    def __init__(self, page: Page):
        self.page = page

        # Creates the side menu
        self.menu = SideMenu(self)

        # Creates App Bar
        self.bar = Appbar(self)
        self.page.navigation_bar = self.bar.build()

        """
        creates instances of views and passes the class itself as a parameter
        for all of them, facilitating communication between all classes
        """
        self.login = Login(self)
        self.home = Home(self)
        self.users = Users(self)
        self.customers = Customers(self)
        self.register_customer = RegisterCustomer(self)
        self.products = Products(self)
        self.register_product = RegisterProducts(self)
        self.sales = Sales(self)
        self.register_sales = RegisterSales(self)

        # Creates instances of dialogs
        self.pick_files_dialog = FilePicker()
        self.save_file_dialog = FilePicker()
        self.get_directory_dialog = FilePicker()
        # hide all dialogs in overlay
        self.page.overlay.extend([
            self.pick_files_dialog,
            self.save_file_dialog,
            self.get_directory_dialog,
        ])

        # Creates dict of routes:
        self.routes = {
            '/': self.login,
            '/home': self.home,
            '/users': self.users,
            '/customers': self.customers,
            '/register_customer': self.register_customer,
            '/products': self.products,
            '/register_product': self.register_product,
            '/sales': self.sales,
            '/register_sales': self.register_sales,
        }

        # Creates dict of method to initialize the Views:
        self.calls = {
            '/': self.login.initialize,
            '/home': self.home.initialize,
            '/users': self.users.initialize,
            '/customers': self.customers.initialize,
            '/register_customer': self.register_customer.initialize,
            '/products': self.products.initialize,
            '/register_product': self.register_product.initialize,
            '/sales': self.sales.initialize,
            '/register_sales': self.register_sales.initialize,
        }

        # App's body:
        self.container = Container(expand=True, content=self.routes['/'])
        self.body = Row(
            expand=True,
            controls=[
                self.menu,
                VerticalDivider(width=1),
                self.container,
            ],
        )

        # Create configs
        self.config = Config(self)

    def route_change(self, e):
        # Change View:
        self.container.content = self.routes[e.route]
        # self.body.update()
        self.page.update()

        # Initialize the View
        self.calls[e.route]()

        self.page.update()
