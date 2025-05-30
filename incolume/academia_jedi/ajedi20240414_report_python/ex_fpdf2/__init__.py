"""Module."""

from inspect import stack
from pathlib import Path
from typing import NoReturn

from fpdf import FPDF

__author__ = '@britodfbr'  # pragma: no cover


def example_minimal() -> NoReturn:
    """Exemplo mínimo de relatório com fpdf2."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 16)
    pdf.cell(40, 10, 'Hello World!')
    pdf.output(Path(stack()[0][3]).with_suffix('.pdf').as_posix())


def example_report1() -> NoReturn:
    """Exemplo relatório com fpdf2."""
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 16)
    pdf.cell(40, 10, 'Hello World!')
    pdf.set_font('helvetica', size=16)
    pdf.cell(40, 10, 'Hello World!')
    pdf.output(Path(stack()[0][3]).with_suffix('.pdf').as_posix())


class PDF(FPDF):
    """Class customized."""

    def header(self):
        """Header for PDF."""
        # Rendering logo:
        logo = Path(__file__).parent.joinpath('..', 'images', 'jedi_logo.png')
        self.image(logo, 10, 8, 33)
        # Setting font: helvetica bold 15
        self.set_font('helvetica', 'B', 15)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, 'Title', border=1, align='C')
        # Performing a line break:
        self.ln(35)

    def footer(self):
        """Footer for PDF."""
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font('helvetica', 'I', 8)
        # Printing page number:
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')


def tuto02() -> NoReturn:
    """Aqui um exemplo de duas páginas com cabeçalho, rodapé e logótipo."""
    # Instantiation of inherited class
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Times', size=12)
    for i in range(1, 41):
        pdf.cell(
            0,
            10,
            f'Printing line number {i}',
            new_x='LMARGIN',
            new_y='NEXT',
        )
    pdf.output(Path(stack()[0][3]).with_suffix('.pdf').as_posix())
