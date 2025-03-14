"""Module."""
# ruff: noqa: T201

import logging

from incolume.academia_jedi.ajedi20221210_html_parsin import resp
from parsel import Selector

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
