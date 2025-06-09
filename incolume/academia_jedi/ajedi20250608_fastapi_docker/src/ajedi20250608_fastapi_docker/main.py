"""FastAPI application example with a simple endpoint."""

from ajedi20250608_fastapi_docker import main
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def hello(name: str = 'World') -> str:
    """Return a greeting message.

    Args:
        name (str): The name to greet. Defaults to 'World'.

    Returns:
        str: A greeting message.
    """
    return f'{main()} - Hello, {name}!'
