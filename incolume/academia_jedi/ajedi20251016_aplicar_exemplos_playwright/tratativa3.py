"""Exemplo 3."""

from icecream import ic
from playwright.sync_api import Locator, expect, sync_playwright, Page

str_html = ''


def action(page: Page) -> None:
    """Iteration over list locator."""
    elements = page.locator('table#tblProcessosRecebidos:has(a)').all()

    for i, element in enumerate(elements):
        ic(i, element)


def actions(url: str = 'http://localhost:8000') -> None:
    """Automation."""
    with sync_playwright() as handler:
        browser = handler.chromium.launch(headless=False)
        ic()
        with browser.new_context() as context:
            page = context.new_page()
            page.goto(url)
            ic()
            action(page)
            # process_receved = page.locator('#tblProcessosRecebidos')
            # expect(process_receved).to_be_visible()
            # ic(process_receved)
