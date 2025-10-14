"""Module."""
import tempfile
from pathlib import Path
from typing import Any

from icecream import ic
from playwright.sync_api import sync_playwright


html_text="""
<html>
<head><title>Fake page</title></head>
<body>
<table border=1>
  <tbody>
    <tr>
      <td>&nbsp;</td>
      <td><img src='https://www.gov.br/favicon.ico'></td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td><img src='https://www.gov.br/favicon.ico'></td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td><img src='https://www.gov.br/favicon.ico'></td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td><img src='https://protocolosip.presidencia.gov.br/favicon.ico'></td>
      <td>
        <input lotsofuselesstext value="Steve">

      </td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td><img src='https://www.gov.br/favicon.ico'></td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td><img src='https://www.gov.br/favicon.ico'></td>
      <td>&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;</td>
      <td><img src='https://protocolosip.presidencia.gov.br/favicon.ico'></td>
      <td>
        <input lotsofuselesstext value="Mark">

      </td>
      <td>&nbsp;</td>
    </tr>
  </tbody>
</table>
</body>
</html>
"""

dout = Path(tempfile.gettempdir())/Path(__file__).parent.stem

def config():
    """Config it."""
    dsite: Path = dout/'site-fake'
    dsite.mkdir(parents=True, exist_ok=True)
    site = dsite/'index.html'
    site.write_text(html_text)

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
    url = (
        url
        or 'http://localhost:8000'
    )
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

def automation1(url: str = '')-> None:
    """Automation."""
    url = url or 'http://localhost:8000'
    with sync_playwright() as handler:
        browser = handler.webkit.launch(headless=False)
        with browser.new_context() as context:
            page = context.new_page()
            page.goto(url)
            # expect(page.get_by_text("Welcome, John!")).to_be_visible()
            page.screenshot(path=filename())



def main() -> None:
    """Run it."""
    ic('Hello from ajedi20251013-getting-elements-in-a-table-with-playwright!')
    config()
    ic(html_text)
    automation1()






if __name__ == "__main__":
    main()
