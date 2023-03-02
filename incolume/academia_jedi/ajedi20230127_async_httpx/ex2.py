from time import perf_counter
import httpx
import asyncio
import logging

__author__ = "@britodfbr"  # pragma: no cover


async def fetch():
    urls = [
        "https://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html",
        "https://books.toscrape.com/catalogue/category/books/nonfiction_13/page-2.html",
        "https://books.toscrape.com/catalogue/category/books/nonfiction_13/page-3.html",
        "https://books.toscrape.com/catalogue/category/books/nonfiction_13/page-4.html",
        "https://books.toscrape.com/catalogue/category/books/nonfiction_13/page-5.html",
        "https://books.toscrape.com/catalogue/category/books/nonfiction_13/page-6.html",
        "https://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html",
        "https://books.toscrape.com/catalogue/category/books/fiction_10/index.html",
        "https://books.toscrape.com/catalogue/category/books/fiction_10/page-2.html",
        "https://books.toscrape.com/catalogue/category/books/fiction_10/page-3.html",
        "https://books.toscrape.com/catalogue/category/books/fiction_10/page-4.html",
        "https://books.toscrape.com/catalogue/category/books/default_15/index.html",
        "https://books.toscrape.com/catalogue/category/books/default_15/page-2.html",
        "https://books.toscrape.com/catalogue/category/books/default_15/page-3.html",
        "https://books.toscrape.com/catalogue/category/books/default_15/page-4.html",
        "https://books.toscrape.com/catalogue/category/books/default_15/page-5.html",
        "https://books.toscrape.com/catalogue/category/books/default_15/page-6.html",
        "https://books.toscrape.com/catalogue/category/books/default_15/page-7.html",
        "https://books.toscrape.com/catalogue/category/books/default_15/page-8.html",
    ]

    async with httpx.AsyncClient() as client:
        reqs = [client.get(url) for url in urls]
        results = await asyncio.gather(*reqs)
    return results


def run():
    initial = perf_counter()
    print(asyncio.run(fetch()))
    logging.debug(f"acesso sincrono: {perf_counter() - initial}s")


if __name__ == "__main__":  # pragma: no cover
    run()
