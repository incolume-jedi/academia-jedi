"""Module."""

import logging
import os
from pathlib import Path

import dotenv
from icecream import ic
from incolume.academia_jedi.ajedi20230211_massa_dados_faker_protocol.generator_pessoas import (  # noqa: E501
    massa_pessoas,
)

__author__ = '@britodfbr'  # pragma: no cover


config = dotenv.load_dotenv(dotenv.find_dotenv(filename='dotenv'))
logging.debug(ic(config))

dados_json = massa_pessoas()
logging.debug(ic(dados_json))

dados_dict = massa_pessoas(type='dict')
logging.debug(ic(dados_dict))

fileoutput = (
    Path(__file__).parent / 'databases' / (os.getenv('BASENAME') or 'TestDB')
)
fileoutput.parent.mkdir(exist_ok=True, parents=True)
logging.debug(ic(fileoutput))
