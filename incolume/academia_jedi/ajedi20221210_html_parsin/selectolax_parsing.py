"""Module."""
# ruff: noqa: T201

import logging

from incolume.academia_jedi.ajedi20221210_html_parsin import resp
from selectolax.parser import HTMLParser

html = HTMLParser(resp.text)
logging.info(html.css_first('h1').text)

books = []
for item in html.css('article.product_pod'):
    book = {
        'name': item.css_first('h3 a').attributes['title'],
        'link': item.css_first('a').attrs['href'],
        'price': item.css_first('p.price_color').text,
        'img': item.css_first('img.thumbnail').attributes['src'],
    }
    print(book)
    books.append(book)
logging.debug(books)
