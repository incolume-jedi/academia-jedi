"""Acesso API IBGE - Academia Jedi 20250602."""

import httpx
from icecream import ic
from incolume.academia_jedi import logger

url_api = 'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}'


def get_nome(nome: str, params: dict | None = None) -> dict:
    params = params or {}
    try:
        response = httpx.get(url_api.format(nome=nome), params=params)
        response.raise_for_status()
        logger.info(ic(response.json()))
        return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(
            f'HTTP error occurred: {e.response.status_code} - {e.response.text}',
        )


def main() -> None:
    """Main function to execute the script."""
    print('Hello from ajedi20250602-acesso-api-ibge!')  # noqa: T201
    get_nome('ada')
    get_nome('ana')
    get_nome('eliana')
    get_nome('ricardo')
    (get_nome('ariel', params={'sexo': 'F'}),)
    (get_nome('ariel', params={'sexo': 'M'}),)
    (get_nome('ada', params={'sexo': 'F', 'groupBy': 'UF'}),)
    (get_nome('ada', params={'sexo': 'M', 'groupBy': 'UF'}),)


if __name__ == '__main__':
    main()
