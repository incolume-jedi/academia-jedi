"""FastAPI application example with a simple endpoint."""

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
    return f'Hello, {name}!'
