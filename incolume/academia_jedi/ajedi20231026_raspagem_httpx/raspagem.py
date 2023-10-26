import httpx
from bs4 import BeautifulSoup
from pathlib import Path
from typing import Container
from tempfile import gettempdir


def get_content(url: str) -> Container:
    """Donwload content web."""

    req = httpx.get(url)
    content = req.text
    soup = BeautifulSoup(content, 'html5lib')
    result = soup.select_one('div.corpo_texto_noticia').contents
    result = [line.strip() for line in result if line and isinstance(line, str)]
    # print(result)
    return result

def write_content(fout: Path, content: Container) -> bool:
    soup = BeautifulSoup('', 'html5lib')
    for line in content:
        if line:
            p = soup.new_tag('p')
            p.string = line
            soup.html.body.append(p)
    print(soup.prettify())
    fout.write_bytes(soup.prettify(encoding='utf-8'))
    return True


def run():
    """"""
    url = 'https://www.diariodasleis.com.br/legislacao/federal/exibe_artigo.php?ifl=203526'
    file = Path(gettempdir())/'dim18320616-001.html'
    
    content = get_content(url)
    write_content(file, content)



run()