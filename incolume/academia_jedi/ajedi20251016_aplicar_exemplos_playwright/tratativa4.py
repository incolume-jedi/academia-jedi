"""Exemplo 4."""
import re

from icecream import ic
from playwright.sync_api import Locator, expect, sync_playwright

str_html = ''


def action(elements: list[Locator]) -> None:
    """Iteration over list locator."""
    for i, element in enumerate(elements):
        ic(i, element.text_content())


def actions(url: str = 'http://localhost:8000') -> None:
    """Automation."""
    with sync_playwright() as handler:
        browser = handler.chromium.launch(headless=False)
        ic()
        with browser.new_context() as context:
            page = context.new_page()
            page.goto(url)
            ic()
            process_receved = page.locator('#tblProcessosRecebidos')
            expect(process_receved).to_be_visible()
            ic(process_receved)
            # td = page.get_by_role("td", name=re.compile("submit", re.IGNORECASE)).click()
            td=page.locator('td', has_text=re.compile('.*Visualizado', flags=re.IGNORECASE))
            action(td.all())
            action(process_receved.locator(re.compile('processoVisualizado|processoNaoVisualizado')).all())

