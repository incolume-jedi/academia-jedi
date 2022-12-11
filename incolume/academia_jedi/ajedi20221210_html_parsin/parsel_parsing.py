import requests
from parsel import Selector
from pathlib import Path
from tomli import load
import logging


config = Path(__file__).parent / 'conf.toml'
assert config.exists(), f"Error: {config}"

with config.open('rb') as file:
    url = load(file)["url"]["toscrape"]

logging.debug(url)

resp = requests.get(url=url)
logging.debug(resp)

html =  Selector(text=resp.text)
logging.info(html.css('h1::text').get())

books = []
for item in html.css('article.product_pod'):
    book ={
        'name': item.css('h3 a').attrib['title'],
        'link': item.css('a').attrib['href'],
        'price': item.css('p.price_color::text').get(),
        'img': item.css('img.thumbnail').attrib['src']
    }
    print(book)
    books.append(book)
logging.debug(books)
