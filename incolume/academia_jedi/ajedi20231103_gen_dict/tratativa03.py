""" Acesso a gsheet.

Codificação oriunda de
http://github.com/incolumepy-prospections/incolumepy.dataclass."""

import logging
from itertools import chain
from pathlib import Path
from typing import Iterator

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dataclasses import dataclass

__author__ = "@britodfbr"  # pragma: no cover


@dataclass
class GSheet:
    """GSheet access."""
    __credential: Path = None
    __escopo: Iterator = None

    @property
    def credentials(self) -> Path:
        """Autenticação API Google."""
        return self.__credential

    @credentials.setter
    def credentials(self, file_credential: Path = None) -> None:
        """Autenticação API Google."""
        logging.info('setting: %s', file_credential)
        if not file_credential.is_file():
            logging.debug('not file: %s', file_credential)
            file_credential = Path('~').expanduser().joinpath(
                "projetos",
                "private",
                "authkeys",
                'incolumepy-dev-6ae65605985c.json')
            logging.info('setting: %s', file_credential)
        if not file_credential.is_file():
            logging.debug('not file: %s', file_credential)
            file_credential = Path(__file__).parents[0].joinpath(
                'credentials', 'incolumepy-dev-6ae65605985c.json'
            )
            logging.info('setting: %s', file_credential)
        logging.debug('return: %s', file_credential)
        if not file_credential.is_file():
            msg = 'Credential file not found.'
            logging.error(msg)
            raise FileNotFoundError(msg)
        self.__credential = file_credential

    @property
    def escopo(self):
        """Escope to gsheet."""
        return self.__escopo

    @escopo.setter
    def escopo(self, value: list[str]) -> None:
        """Escope to gsheet."""
        self.__escopo = chain(
            [
                'https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive'
            ],
            value
        )

    @property
    def client_google(self):
        credenciais = ServiceAccountCredentials.from_json_keyfile_name(
            self.credentials, self.escopo)

        # client_google
        gc = gspread.authorize(credenciais)
        return gc

    def drop_sheet(self, spreadsheet, dropthis: bool = False) -> bool:
        """
        Drop Planilha

        :param spreadsheet:
        :param dropthis: bool
        :return: bool
        """
        if dropthis:
            self.client_google.del_spreadsheet(spreadsheet.id)
            return True
        return False

    def load_create_sheet(self, spreadsheetname):
        """
        Carregar/Criar Planilha.

        :return:
        """

        try:
            spreadsheet = self.client_google.open(spreadsheetname)
        except (gspread.exceptions.SpreadsheetNotFound,
                gspread.exceptions.APIError):
            spreadsheet = self.client_google.create(spreadsheetname)

        return spreadsheet

    def permission_sheet(self, spreadsheet, users: list[str]):
        """
        permissões Planilha.

        :param spreadsheet:
        :param users: list[str] lista com email de usuários
        :return:
        """

        list_users = chain([
            'brito@incolume.com.br',
            'britodfbr@gmail.com',
            'dev@incolume.com.br',
            'dataaccess@incolumepy-dev.iam.gserviceaccount.com',
        ], users)
        for user in list_users:
            logging.info(user)
            spreadsheet.share(user, perm_type='user', role='writer')

    def get_url_sheet(self, spreadsheet):
        """
        Link acesso web

        :return:
        """
        result = f'https://docs.google.com/spreadsheets/d/{spreadsheet.id}'
        logging.debug(result)
        return result
