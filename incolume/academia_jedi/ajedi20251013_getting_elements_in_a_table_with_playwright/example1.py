"""Module."""

from __future__ import annotations

import re

from playwright.sync_api import expect, sync_playwright

str_html: str = """<h3>Sign up</h3>
<label>
  <input type="checkbox" /> Subscribe
</label>
<br/>
<button>Submit</button>"""


def actions() -> None:
    """Automation actions."""
    with sync_playwright() as handler:
        browser = handler.chromium.launch(headless=False)
        with browser.new_context() as context:
            page = context.new_page()
            expect(page.get_by_role('heading', name='Sign up')).to_be_visible()
            page.get_by_role('checkbox', name='Subscribe').check()
            page.get_by_role(
                'button',
                name=re.compile('submit', re.IGNORECASE),
            ).click()
