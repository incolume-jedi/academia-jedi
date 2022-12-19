import requests
from bs4 import BeautifulSoup
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

soup =  BeautifulSoup(resp.text, 'lxml')
logging.info(soup.find('h1').text)

books = []
for item in soup.find_all('article', {'class': 'product_pod'}):
    book ={
        'name': item.find('h3').find('a').attrs['title'],
        'link': item.find('a').attrs['href'],
        'price': item.find('p', 'price_color').text,
        'img': item.find('img', 'thumbnail').attrs['src']
    }
    print(book)
    books.append(book)
logging.debug(books)
