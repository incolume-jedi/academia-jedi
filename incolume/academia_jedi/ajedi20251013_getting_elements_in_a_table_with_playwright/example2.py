"""Example 2."""
from __future__ import annotations

from icecream import ic
from playwright.sync_api import sync_playwright


str_html: str = """
<html>
<body>
<table>
  <caption style="caption-side:bottom">Monthly savings</caption>
  <tr>
    <th>Month</th>
    <th>Savings</th>
  </tr>
  <tr>
    <td>January</td>
    <td>$100</td>
    <td><a href='/links/3/1'>0</a></td>
  </tr>
  <tr>
    <td>Fev</td>
    <td>$100</td>
    <td><a href='/links/3/2'>0</a></td>
  </tr>
  <tr>
    <td>Mar</td>
    <td>$100</td>
    <td><a href='/links/3/3'>0</a></td>
  </tr>
  <tr>
    <td>Abr</td>
    <td>$100</td>
    <td><a href='/links/3/4'>0</a></td>
  </tr>
  <tr>
    <td>Jun</td>
    <td>$100</td>
    <td><a href='/links/3/6'>0</a></td>
  </tr>
  <tr>
    <td>Jul</td>
    <td>$100</td>
    <td><a href='/links/3/7'>0</a></td>
  </tr>
  <tr>
    <td>Ago</td>
    <td>$100</td>
    <td><a href='/links/3/8'>0</a></td>
  </tr>
  <tr>
    <td>Set</td>
    <td>$100</td>
    <td><a href='/links/3/9'>0</a></td>
  </tr>
  <tr>
    <td>Out</td>
    <td>$100</td>
    <td><a href='/links/3/10'>0</a></td>
  </tr>
  <tr>
    <td>Nov</td>
    <td>$100</td>
    <td><a href='/links/3/11'>0</a></td>
  </tr>
  <tr>
    <td>Dez</td>
    <td>$100</td>
    <td><a href='/links/3/12'>0</a></td>
  </tr>
  <tr>
    <td>Mai</td>
    <td>$100</td>
    <td><a href='/links/3/5'>0</a></td>
  </tr>
</table>
</body>
</html>
"""


def actions(url: str = '')->None:
    """Automation here."""
    with sync_playwright() as handler:
        browser = handler.chromium.launch(headless=False)
        with browser.new_context() as context:
            page = context.new_page()
            page.goto(url)

            link_locators = page.locator('table.stats_table').get_by_role('link').all()
            for lk in link_locators:
                ic(lk.get_attribute('href'))
