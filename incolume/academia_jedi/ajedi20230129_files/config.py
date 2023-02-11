import dotenv
import os
import logging
from pathlib import Path
from incolume.academia_jedi.ajedi20220925_massa_dados_faker_protocol. \
    generator_pessoas import massa_pessoas


__author__ = "@britodfbr"  # pragma: no cover


config = dotenv.load_dotenv(dotenv.find_dotenv())
logging.debug(config)

dados = massa_pessoas(is_json=False)
logging.debug(dados)

fileoutput = Path.cwd() / 'databases' / os.getenv('BASENAME')
fileoutput.parent.mkdir(exist_ok=True, parents=True)
logging.debug(fileoutput)
