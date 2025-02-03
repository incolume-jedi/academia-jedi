"""Module."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

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
