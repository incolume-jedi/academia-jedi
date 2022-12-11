import requests
from selectolax.parser import HTMLParser
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

html =  HTMLParser(resp.text)
logging.info(html.css_first('h1').text)

books = []
for item in html.css('article.product_pod'):
    book ={
        'name': item.css_first('h3 a').attributes['title'],
        'link': item.css_first('a').attrs['href'],
        'price': item.css_first('p.price_color').text,
        'img': item.css_first('img.thumbnail').attributes['src']
    }
    print(book)
    books.append(book)
logging.debug(books)
