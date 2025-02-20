"""Module."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

import json
import os

from CreateConfig import CreateConfig
from cryptography.fernet import Fernet

# ruff: noqa: A002, ANN001, ANN201, ARG002, BLE001, C901, D101, D102, D107, DTZ005, DTZ011, E501, ERA001, N802, N803, N806, PLR2004, S608, T201, TRY300


class Config:
    def __init__(self, route) -> None:
        self.route = route
        self.host = None
        self.user = None
        self.passwd = None
        self.database = None
        self.port = None

        self.user_name = None
        self.permission = None

        self.company_name = 'NOME DA SUA EMPRESA'
        self.company_adress = 'Endereço completo da sua Empresa aqui'
        self.company_tel = 'Telefone da sua Empresa aqui'
        self.company_email = 'E-mail da sua Empresa aqui'

    def read_file(self):
        with open('data.bin', 'rb') as file:
            readed_key = file.readline().rstrip()
            readed_data = file.read()
        return readed_data, readed_key

    def decrypt_data(self, encrypted_data, key):
        fernet = Fernet(key)
        return fernet.decrypt(encrypted_data).decode()

    def set_config_data(self, data):
        self.host = data['host']
        self.user = data['user']
        self.passwd = data['passwd']
        self.database = data['database']
        self.port = data['port']

    def set_permissions(self, name, permission):
        self.route.config.user_name = name
        self.route.config.permission = permission

        self.route.menu.nnrail.destinations[2].visible = (
            self.route.config.permission == 'Admin'
        )
        self.route.menu.nnrail.update()

    def open_config_db(self):
        dialog = CreateConfig(self.route)
        self.route.page.dialog = dialog
        dialog.open = True
        self.route.page.update()

    def initialize(self):
        if os.path.exists('data.bin'):  # noqa: PTH110
            readed_data, readed_key = self.read_file()
            decrypted_data = self.decrypt_data(readed_data, readed_key)
            config_dict = json.loads(decrypted_data)
            self.set_config_data(config_dict)
        else:
            self.open_config_db()
