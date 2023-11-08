"""Codificação oriunda de http://github.com/incolumepy-prospections/incolumepy.dataclass."""
import logging
from pathlib import Path
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dataclasses import dataclass

__author__ = "@britodfbr"  # pragma: no cover


class GSheet:
    """GSheet access."""
    __credential: Path = None
    __escopo: list = None

    @property
    def credentials(self) -> Path:
        """Autenticação API Google."""
        return self.credentials

    @credentials.setter
    def credentials(self, file_credential: Path = None) -> None:
        """Autenticação API Google."""
        logging.info('setting: %s', file_credential)
        if not file_credential.is_file():
            logging.debug('not file: %s', file_credential)
            file_credential = Path('~').expanduser().joinpath(
                "projetos",
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
        self.__credential = file_credential

    @property
    def escopo(self):
        """Escope to gsheet."""
        return self.__escopo


    @escopo.setter
    def escopo(self, value: list[str]) -> None:
        """Escope to gsheet."""
        self.__escopo = ['https://spreadsheets.google.com/feeds',
                  'https://www.googleapis.com/auth/drive'] + value

    @property
    def client_google(self):
        credenciais = ServiceAccountCredentials.from_json_keyfile_name(
            self.credentials, self.escopo)

        # client_google
        gc = gspread.authorize(credenciais)
        return gc

    # TODO corrigir daqui para baixo.
    def drop_sheet(self, spreadsheet, dropthis: bool = False):
        """
        Drop Planilha

        :param spreadsheet:
        :param dropthis:
        :return:
        """
        if dropthis:
            gc = get_client_google()
            gc.del_spreadsheet(spreadsheet.id)
            return True
        return False


    def load_create_sheet(self, spreadsheetname):
        """
        Carregar/Criar Planilha.

        :return:
        """

        gc = get_client_google()
        try:
            spreadsheet = gc.open(spreadsheetname)
        except (gspread.exceptions.SpreadsheetNotFound,
                gspread.exceptions.APIError):
            spreadsheet = gc.create(spreadsheetname)

        return spreadsheet


    def permission_sheet(self, spreadsheet):
        """
        permissões Planilha.

        :param spreadsheet:
        :return:
        """

        users = [
            'brito@incolume.com.br', 
            'britodfbr@gmail.com',
            'dev@incolume.com.br', 
            'dataaccess@incolumepy-dev.iam.gserviceaccount.com',
        ]
        for user in users:
            spreadsheet.share(user, perm_type='user', role='writer')


    def get_url_sheet(self, spreadsheet):
        """
        Link acesso web

        :return:
        """
        result = f'https://docs.google.com/spreadsheets/d/{spreadsheet.id}'
        return result
