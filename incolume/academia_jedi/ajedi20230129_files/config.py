import dotenv
import os
import logging
from pathlib import Path
from incolume.academia_jedi.ajedi20230211_massa_dados_faker_protocol.generator_pessoas import (
    massa_pessoas,
)


__author__ = "@britodfbr"  # pragma: no cover


config = dotenv.load_dotenv(dotenv.find_dotenv())
logging.debug(config)

dados_json = massa_pessoas()
logging.debug(dados_json)

dados_dict = massa_pessoas(type="dict")
logging.debug(dados_dict)

fileoutput = Path(__file__).parent / "databases" / os.getenv("BASENAME")
fileoutput.parent.mkdir(exist_ok=True, parents=True)
logging.debug(fileoutput)
