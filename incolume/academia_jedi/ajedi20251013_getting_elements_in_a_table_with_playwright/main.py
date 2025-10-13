"""Module."""
from inspect import stack
from pathlib import Path
import tempfile

from icecream import ic

html_text="""
<html>
<head><title>Fake page</title></head>
<body>
<table>
  <tbody>
    <tr>
    <tr>
    <tr>
    <tr>
      <td>
      <td>
      <td>
        <input lotsofuselesstext value="Steve">
        <img>
      </td>
      <td>
    </tr>
    <tr>
    <tr>
    <tr>
      <td>
      <td>
      <td>
        <input lotsofuselesstext value="Mark">
        <img>
      </td>
      <td>
    </tr>
  </tbody>
</table>
</body>
</html>
"""

def config():
    """Config it."""
    dsite: Path = Path(tempfile.gettempdir())/Path(__file__).parent.stem/'site-fake'
    dsite.mkdir(parents=True, exist_ok=True)
    site = dsite/'index.html'
    site.write_text(html_text)




def main() -> None:
    """Run it."""
    ic("Hello from ajedi20251013-getting-elements-in-a-table-with-playwright!")
    config()
    ic(html_text)


if __name__ == "__main__":
    main()
