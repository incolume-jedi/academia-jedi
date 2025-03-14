"""Module."""
# ruff: noqa: T201

import logging

import requests
from incolume.academia_jedi.ajedi20221210_html_parsin import config, timeout
from parsel import Selector
from tomli import load

with config.open('rb') as file:
    url = load(file)['url']['toscrape']

logging.debug(url)

resp = requests.get(url=url, timeout=timeout)
logging.debug(resp)

html = Selector(text=resp.text)
logging.info(html.css('h1::text').get())

books = []
for item in html.css('article.product_pod'):
    book = {
        'name': item.css('h3 a').attrib['title'],
        'link': item.css('a').attrib['href'],
        'price': item.css('p.price_color::text').get(),
        'img': item.css('img.thumbnail').attrib['src'],
    }
    print(book)
    books.append(book)
logging.debug(books)
