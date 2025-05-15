"""Estudo com biblioteca fake_useragent."""

from fake_useragent import UserAgent
from icecream import ic

ua = UserAgent()

if __name__ == '__main__':
    ic(ua.random)
