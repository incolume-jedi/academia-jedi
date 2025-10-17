"""Exemplo 1."""

from icecream import ic
from playwright.sync_api import Locator, expect, sync_playwright


def action1(elements: list[Locator]) -> None:
    """Iteration over list locator."""
    for element in elements:
        ic(element.text_content())

def action2(elements: list[Locator]) -> None:
    """Iteration over list locator."""
    for element in elements:
        ic(element.inner_html())

def action3(elements: list[Locator]) -> None:
    """Iteration over list locator."""
    for element in elements:
        ic(element.all_text_contents())


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
            anchors = process_receved.locator('a').all()

            action1(anchors)
            action2(anchors)
            action3(anchors)
            action1(process_receved.locator('//td[3]').all())
            action2(process_receved.locator('//td[3]').all())
