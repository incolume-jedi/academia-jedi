"""Module."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

from flet import (
    Container,
    Icon,
    IconButton,
    NavigationRail,
    NavigationRailDestination,
    NavigationRailLabelType,
    UserControl,
    border_radius,
    icons,
    padding,
)
from SetGeneralConfig import SetGeneralConfig


# ruff: noqa: ARG002 A002 DTZ011 C901 T201 ANN201 ERA001 D101 D102 D107 E501 PLR2004
class SideMenu(UserControl):
    def __init__(self, route):
        super().__init__()
        self.route = route

        self.cont = Container(
            padding=padding.all(5),
            # bgcolor=colors.ON_INVERSE_SURFACE,
            border_radius=border_radius.all(5),
            visible=False,
        )
        self.nnrail = NavigationRail(
            extended=False,
            label_type=NavigationRailLabelType.NONE,
            min_width=56,
            min_extended_width=160,
            bgcolor='transparent',
            leading=IconButton(
                icon=icons.SWAP_HORIZ_ROUNDED,
                icon_size=40,
                tooltip='Mostrar/Ocultar Opções',
                on_click=self.menu_clicked,
            ),
            group_alignment=-0.95,
            destinations=[
                NavigationRailDestination(
                    icon=icons.COTTAGE_OUTLINED,
                    selected_icon=icons.COTTAGE,
                    label='Home',
                ),
                NavigationRailDestination(
                    icon_content=Icon(icons.PERM_CONTACT_CALENDAR_OUTLINED),
                    selected_icon_content=Icon(icons.PERM_CONTACT_CALENDAR),
                    label='Clientes',
                ),
                NavigationRailDestination(
                    icon_content=Icon(icons.PERSON_OUTLINED),
                    selected_icon_content=Icon(icons.PERSON_ROUNDED),
                    label='Usuários',
                ),
                NavigationRailDestination(
                    icon_content=Icon(icons.INVENTORY_2_OUTLINED),
                    selected_icon_content=Icon(icons.INVENTORY),
                    label='Produtos',
                ),
                NavigationRailDestination(
                    icon_content=Icon(icons.SHOPPING_CART_OUTLINED),
                    selected_icon_content=Icon(icons.SHOPPING_CART),
                    label='Vendas',
                ),
                # NavigationRailDestination(
                #     icon=icons.SETTINGS_OUTLINED, selected_icon_content=Icon(icons.SETTINGS), label='Configurações',
                # ),
            ],
            trailing=IconButton(
                icon=icons.SETTINGS,
                on_click=self.show_config_page,
            ),
            on_change=self.nav_clicked,
        )
        self.cont.content = self.nnrail

    def build(self):
        return self.cont

    def menu_clicked(self, e):
        self.nnrail.extended = not self.nnrail.extended
        self.update()

    def nav_clicked(self, e):
        if e.control.selected_index == 0:
            self.page.go('/home')
            self.route.bar.set_title('Pagina Inicial')
            self.route.page.update()
            self.update()
            return
        if e.control.selected_index == 1:
            self.page.go('/customers')
            self.route.bar.set_title('Clientes')
            self.route.page.update()
            self.update()
            return
        if e.control.selected_index == 2:
            self.page.go('/users')
            self.route.bar.set_title('Controle de Usuários')
            self.route.page.update()
            self.update()
            return
        if e.control.selected_index == 3:
            self.page.go('/products')
            self.route.bar.set_title('Produtos')
            self.route.page.update()
            self.update()
            return
        if e.control.selected_index == 4:
            self.page.go('/sales')
            self.route.bar.set_title('Vendas')
            self.route.page.update()
            self.update()

    def show_config_page(self, e):
        dialog = SetGeneralConfig(self.route)
        self.route.page.dialog = dialog
        dialog.open = True
        self.route.page.update()
