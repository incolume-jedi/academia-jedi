"""Acesso API IBGE - Academia Jedi 20250602."""

import httpx
from config import settings
from icecream import ic
from incolume.academia_jedi import logger

url_api = 'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}'

ic.configureOutput(prefix='[ajedi20250602-acesso-api-ibge] ')
ic.disable()
if settings.DEBUG_MODE:
    ic.enable()


def get_api(params: dict | None = None, url_api: str = '') -> dict:
    """Get API information."""
    params = params or {}
    try:
        response = httpx.get(url_api, params=params)
        response.raise_for_status()
        logger.info(ic(response.json()))
        return response.json()
    except httpx.HTTPStatusError as e:
        logger.error(
            f'HTTP error occurred: {e.response.status_code}'
            f' - {e.response.text}',
        )


def get_nome(nome: str, params: dict | None = None) -> dict:
    """Get name information from IBGE API."""
    params = params or {}
    return get_api(url_api=url_api.format(nome=nome), params=params) or {}


def get_region(
    params: dict | None = None,
    url_api: str = 'https://servicodados.ibge.gov.br/api/v1/localidades/distritos',
) -> dict:
    """Get region information for a given name."""
    params = params or {'view': 'nivelado'}
    return get_api(url_api=url_api, params=params)


def get_uf(
    params: dict | None = None,
    url_api: str = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados',
) -> dict:
    """Get UF information."""
    params = params or {'view': 'nivelado'}
    return get_api(url_api=url_api, params=params)


def get_uf_by_id(
    uf_id: str | int,
    params: dict | None = None,
    url_api: str = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados',
) -> dict:
    """Get UF information."""
    params = params or {'view': 'nivelado'}
    uf_id = int(uf_id) if isinstance(uf_id, str) and uf_id.isdigit() else uf_id
    for uf in get_api(url_api=url_api, params=params):
        if uf.get('UF-id') == uf_id:
            ic(uf)
            return uf
    return {}


def main() -> None:
    """Main function to execute the script."""
    print('Hello from ajedi20250602-acesso-api-ibge!')
    get_uf_by_id(53)


if __name__ == '__main__':
    main()
