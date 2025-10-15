"""Module."""

import contextlib
import tempfile
from pathlib import Path
from subprocess import Popen
from typing import Any

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

dout = Path(tempfile.gettempdir()) / Path(__file__).parent.stem


def config() -> Path:
    """Config it."""
    dsite: Path = dout / 'site-fake'
    dsite.mkdir(parents=True, exist_ok=True)
    site = dsite / 'index.html'
    site.write_text(html_text)
    return site


def filename(**kwargs: [str, Any]) -> Path:
    """Filename.

    Args:
        kwargs:
          contains:
            mode: OpenBinaryMode = "w+b",
            buffering: int = -1,
            encoding: str | None = None,
            newline: str | None = None,
            suffix: AnyStr@NamedTemporaryFile = .png,
            prefix: AnyStr@NamedTemporaryFile = print-screen-,
            dir: GenericPath[AnyStr@NamedTemporaryFile] = $OSTEMPFILEDIR,
            delete: bool = True,
            errors: str | None = None

    """
    args: dict[str, Any] = {
        'mode': kwargs.get('mode', 'w+b'),
        'buffering': kwargs.get('buffering', -1),
        'encoding': kwargs.get('encoding'),
        'suffix': kwargs.get('suffix', '.png'),
        'prefix': kwargs.get('prefix', 'print-screen-'),
        'dir': kwargs.get('dir', dout),
        'delete': kwargs.get('delete', True),
        'errors': kwargs.get('errors'),
    }
    with tempfile.NamedTemporaryFile(**args) as fl:
        return fl.name


def automation0(
    username: str,
    password: str,
    url: str = '',
    department: str = '',
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


def automation1(url: str = '') -> None:
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
            child = page.get_by_text("Welcome, John")
            result.append(child)
            result.append(page.get_by_role("listitem").filter(has=child))

            ic(result[-1])
            result.append(page.get_by_text("Welcome, John").locator('xpath=..'))
            ic(result[-1])
            for elem in result[0]:
                ic(elem)



def main() -> None:
    """Run it."""
    ic('Hello from ajedi20251013-getting-elements-in-a-table-with-playwright!')
    site = config()
    with contextlib.suppress(FileNotFoundError):
        Popen(f'python -m http.server 8000 -d {site.parent}', shell=True)
    ic(html_text)
    automation1()


if __name__ == '__main__':
    main()
