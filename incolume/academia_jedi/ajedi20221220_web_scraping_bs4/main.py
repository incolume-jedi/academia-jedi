# import scrap_imdb
from tempfile import gettempdir
from pathlib import Path
from my_scrap_imdb import scraping_ranking
from my_scrap_imdb1 import scraping_ranking1
from my_scrap_imdb2 import ScrapingIMDB

__author__ = "@britodfbr"  # pragma: no cover

if __name__ == "__main__":  # pragma: no cover
    scraping_ranking(excel_output=Path(gettempdir()) / "abc.xlsx")
    scraping_ranking1(excel_output=Path(gettempdir()) / "bcd.xlsx")
    scrap_imdb = ScrapingIMDB()
    scrap_imdb.connect().get_soup().get_movies().save_excel(
        excel_output=Path(gettempdir()) / "xpto.xlsx"
    )
    ScrapingIMDB().scraping(excel_output="a1b2.xlsx")
