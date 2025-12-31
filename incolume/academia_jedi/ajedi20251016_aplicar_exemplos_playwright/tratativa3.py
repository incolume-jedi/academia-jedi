"""Exemplo 3."""

from icecream import ic
from playwright.sync_api import Locator, Page, expect, sync_playwright

str_html = ''


def action(page: Page) -> None:
    """Iteration over list locator."""
    elements = page.locator('table#tblProcessosRecebidos:has(a)').all()

    for i, element in enumerate(elements):
        ic(i, element)


def action1(elements: list[Locator]) -> None:
    """Iteration over list locator."""
    for i, element in enumerate(elements):
        ic(i, element.inner_html())


def action2(elements: list[Locator]) -> None:
    """Iteration over list locator."""
    for i, element in enumerate(elements):
        ic(i, element.get_attribute('aria-label'))


def action3(elements: list[Locator]) -> None:
    """Iteration over list locator."""
    for i, element in enumerate(elements):
        ic(i, element.evaluate_all('list => list.map(el => el.href)'))


def action4(elements: list[Locator]) -> None:
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
            action(page)
            process_receved = page.locator('#tblProcessosRecebidos')
            expect(process_receved).to_be_visible()
            ic(process_receved)
            action1(
                process_receved.locator('//td[3]').get_by_role('link').all()
            )
            action2(
                process_receved.locator('//td[3]').get_by_role('link').all()
            )
            action3(
                process_receved.locator('//td[3]').get_by_role('link').all()
            )
            action4(
                process_receved.locator('//td[3]').get_by_role('link').all()
            )
