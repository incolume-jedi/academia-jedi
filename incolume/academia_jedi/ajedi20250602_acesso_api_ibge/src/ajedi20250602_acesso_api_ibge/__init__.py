"""Acesso API IBGE - Academia Jedi 20250602."""

import httpx
from incolume.academia_jedi import logger
from icecream import ic


url_api = 'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}'

def get_nome(nome: str) -> dict:
    try:
        response = httpx.get(url_api.format(nome=nome))
        response.raise_for_status()
        logger.info(ic(response.json()))
        return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(f'HTTP error occurred: {e.response.status_code} - {e.response.text}')

def main() -> None:
    """Main function to execute the script."""
    print('Hello from ajedi20250602-acesso-api-ibge!')  # noqa: T201
    get_nome('ada')
    get_nome('ana')  
    get_nome('eliana')  
    get_nome('ricardo')  


if __name__ == '__main__':
    main()
