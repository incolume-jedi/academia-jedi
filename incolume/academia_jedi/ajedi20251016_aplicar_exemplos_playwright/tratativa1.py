"""Exemplo 1."""
from icecream import ic

from playwright.sync_api import expect, sync_playwright


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

            for e in anchors:
                ic(e.text_content())

            for element in anchors:
                ic(element.inner_html())

            for elem in anchors:
                ic(elem.all_text_contents())

            for el in process_receved.locator('//td[3]').all():
                ic(el.text_content())

            for elt in process_receved.locator('//td[3]').all():
                ic(elt.inner_html())
