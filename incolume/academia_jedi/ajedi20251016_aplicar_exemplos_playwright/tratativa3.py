"""Exemplo 3."""

import sys
from inspect import stack

from icecream import ic
from incolume.academia_jedi.utils import check_web_resource
from playwright.sync_api import Page, sync_playwright

str_html = ''


def action(page: Page) -> None:
    """Iteration over list locator."""
    elements = page.locator('table#tblProcessosRecebidos:has(a)').all()

    for i, element in enumerate(elements):
        ic(i, element)


def actions(url: str = 'http://localhost:8000') -> None:
    """Automation."""
    if error_code := (not check_web_resource(url)):
        ic(stack()[0][3], error_code)
        sys.exit(error_code)

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
