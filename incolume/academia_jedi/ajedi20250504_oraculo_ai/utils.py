"""Utils."""

from collections.abc import Callable
from pathlib import Path

from langchain_community.document_loaders import (
    CSVLoader,
    PyPDFLoader,
    TextLoader,
    UnstructuredExcelLoader,
    WebBaseLoader,
    YoutubeLoader,
)


def midia_loader(midia: str, *, loader: Callable = CSVLoader) -> str:
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


def load_yt(
    video_id: str,
    *,
    add_video_info: bool = False,
    language: None | list[str] = None,
    loader: Callable = YoutubeLoader,
) -> str:
    """Get the name of the file from the url.

    Args:
        video_id (str): The ID of the YouTube video to load.
        add_video_info (bool, optional): Whether to include video metadata in
          the output. Defaults to False.
        language (None | list[str], optional): List of languages for subtitles.
          Defaults to ['pt'].
        loader (Callable, optional): The loader class to use for loading the
            video. Defaults to YoutubeLoader.

    Returns:
        str: The content of the video as a string.
    """
    language = language or ['pt']
    return '\n\n'.join(
        doc.page_content
        for doc in loader(video_id, add_video_info, language=language).load()
    )


def load_csv(
    file_path: Path,
    *,
    autodetect_encoding: bool = True,
    loader: Callable = CSVLoader,
) -> str:
    """Load a CSV file.

    Args:
        file_path (Path): The path to the CSV file.
        autodetect_encoding (bool, optional): Whether to automatically detect
            the file encoding. Defaults to True.
        loader (Callable, optional): The loader class to use for loading the
            CSV file. Defaults to CSVLoader.

    Returns:
        str: The content of the CSV file as a string.
    """
    return '\n\n'.join(
        doc.page_content
        for doc in loader(
            file_path=file_path,
            autodetect_encoding=autodetect_encoding,
        ).load()
    )


def load_pdf(
    file_path: Path,
    *,
    loader: Callable = PyPDFLoader,
) -> str:
    """Load a PDF file.

    Args:
        file_path (Path): The path to the PDF file.
        loader (Callable, optional): The loader class to use for loading the
            PDF file. Defaults to PyPDFLoader.

    Returns:
        str: The content of the PDF file as a string.
    """
    return '\n\n'.join(
        doc.page_content
        for doc in loader(
            file_path=file_path,
        ).load()
    )


def load_txt(
    file_path: Path,
    *,
    autodetect_encoding: bool = True,
    loader: Callable = TextLoader,
) -> str:
    """Load a text file.

    Args:
        file_path (Path): The path to the text file.
        autodetect_encoding (bool, optional): Whether to automatically detect
            the file encoding. Defaults to True.
        loader (Callable, optional): The loader class to use for loading the
            text file. Defaults to TextLoader.

    Returns:
        str: The content of the text file as a string.
    """
    return '\n\n'.join(
        doc.page_content
        for doc in loader(
            file_path=file_path,
            autodetect_encoding=autodetect_encoding,
        ).load()
    )


def load_excel(
    file_path: Path,
    *,
    mode: str = '',
    autodetect_encoding: bool = True,
    loader: Callable = UnstructuredExcelLoader,
) -> str:
    """Load a excel file."""
    mode = mode or 'elements'

    return '\n\n'.join(
        doc.page_content
        for doc in loader(
            file_path=file_path,
            mode=mode,
            autodetect_encoding=autodetect_encoding,
        ).load()
    )
