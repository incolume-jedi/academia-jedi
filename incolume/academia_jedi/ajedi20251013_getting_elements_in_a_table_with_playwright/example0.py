"""Module."""

from __future__ import annotations

from icecream import ic
from playwright.sync_api import expect, sync_playwright

html_text = """
<html>
<head><title>Fake page</title></head>
<body>
<table border=1>
  <tbody>
    <thead>
      <td>id</td>
      <td>ico</td>
      <td>field</td>
      <td>name</td>
    </thead>
    <tr>
      <td>1</td>
      <td><img src='https://www.gov.br/favicon.ico'></td>
      <td>&nbsp;</td>
      <td>Steve</td>
    </tr>
    <tr>
      <td>2</td>
      <td><img src='https://www.gov.br/favicon.ico'></td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>3</td>
      <td><img src='https://www.gov.br/favicon.ico'></td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>4</td>
      <td><img src='https://protocolosip.presidencia.gov.br/favicon.ico'></td>
      <td>
        <input name=lotsofuse id=lesstext value="Steve">

      </td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>5</td>
      <td><img src='https://www.gov.br/favicon.ico'></td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>6</td>
      <td><img src='https://www.gov.br/favicon.ico'></td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>7</td>
      <td><img src='https://protocolosip.presidencia.gov.br/favicon.ico'></td>
      <td>
        <input id=lotsofuse name=lesstext value="Mark">

      </td>
      <td>&nbsp;<label>Welcome, John!<lable></td>
    </tr>
  </tbody>
  <caption>Table demonstration</caption>
</table>
</body>
</html>
"""


def automation0(
    username: str,
    password: str,
    url: str = '',
    department: str = '',
    *,
    filename: callable | None = None,
) -> None:
    """Automation."""
    url = url or 'http://localhost:8000'
    department = department or 'PR'
    ic(username, department)
    with sync_playwright() as handler:
        browser = handler.chromium.launch(headless=False)
        with browser.new_context() as context:
            page = context.new_page()
            page.goto(url)
            ic(page.title())
            page.screenshot(path=filename())
            page.get_by_role('textbox', name='Usuário').fill(username)
            page.get_by_role('textbox', name='Senha').fill(password)
            page.locator('#selOrgao').select_option(department)
            page.get_by_role('button', name='ACESSAR').click()
            page.screenshot(path=filename())


def automation1(url: str = '', *, filename: callable | None = None) -> None:
    """Automation."""
    url = url or 'http://localhost:8000'
    result: list = []
    with sync_playwright() as handler:
        browser = handler.webkit.launch(headless=False)
        with browser.new_context() as context:
            page = context.new_page()
            page.goto(url)
            page.screenshot(path=filename())
            ic(expect(page.get_by_text('Steve')).to_be_visible())
            ic(expect(page.get_by_text('Table demonstration')).to_be_visible())
            child = page.get_by_text('Welcome, John')
            result.append(child)
            result.append(page.get_by_role('listitem').filter(has=child))

            ic(result[-1])
            result.append(
                page.get_by_text('Welcome, John').locator('xpath=..'),
            )
            ic(result[-1])
            result.append(page.get_by_role('table').all())
            ic(result[-1])
            result.append(page.locator('tr >> nth=0'))
            ic(result[-1].content)
