"""Utils."""

from collections.abc import Callable

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    WebBaseLoader,
    YoutubeLoader,
)
from langchain_community.document_loaders.csv_loader import CSVLoader


def midia_loader(midia: str, loader: Callable = CSVLoader) -> str:
    """Load the media file.

    Args:
        midia (str): _description_
        loader (Callable, optional): _description_. Defaults to CSVLoader.

    Returns:
        str: _description_
    """
    loader = (
        loader
        if loader
        in [CSVLoader, WebBaseLoader, YoutubeLoader, PyPDFLoader, TextLoader]
        else CSVLoader
    )
    content = loader.load(midia)
    return '\n\n'.join([doc.page_content for doc in content])


def load_web(url: str, loader: Callable = WebBaseLoader) -> str:
    """Get the name of the file from the url.

    Args:
        url (str): _description_
        loader (Callable, optional): The loader class to use for loading the
            URL. Defaults to WebBaseLoader.
            Defaults to WebBaseLoader.

    Returns:
        str: _description_
    """
    return '\n\n'.join(doc.page_content for doc in loader(url).load())
