"""Module."""
# ruff: noqa: T201

import logging

from bs4 import BeautifulSoup
from incolume.academia_jedi.ajedi20221210_html_parsin import resp

soup = BeautifulSoup(resp.text, 'html5lib')
logging.info(soup.find('h1').text)

books = []
for item in soup.find_all('article', {'class': 'product_pod'}):
    book = {
        'name': item.find('h3').find('a').attrs['title'],
        'link': item.find('a').attrs['href'],
        'price': item.find('p', 'price_color').text,
        'img': item.find('img', 'thumbnail').attrs['src'],
    }
    print(book)
    books.append(book)
logging.debug(books)
