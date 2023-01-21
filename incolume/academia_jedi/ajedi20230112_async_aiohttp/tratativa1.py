import aiohttp
import asyncio

url = {
    "CF": "https://www.camara.leg.br/legislacao/busca?"
    "&geral="
    "&ano="
    "&ordenacao=relevancia:DESC"
    "&abrangencia=Legisla%C3%A7%C3%A3o%20Federal"
    "&tipo=Lei%20Ordin%C3%A1ria"
    "&dataInicio="
    "&dataFim="
    "&origem="
    "&situacao="
    "&numero="
    "&pagina={}",
    "LEXML": None,
    "SICON": None,
    "NORMASLEG": "",
}


async def get_page(url: str = ""):
    url = url or "http://httpbin.org"
    with aiohttp.ClientSession as session:
        req = await session.get(url)
        return req


def main():
    pass


def run():
    main()


if __name__ == "__main__":  # pragma: no cover
    run()
