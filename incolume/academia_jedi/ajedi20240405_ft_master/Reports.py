"""Module."""

# ruff: noqa: A001 A002 ANN001 ANN002 ANN003 ANN201 ANN202 ANN204 ANN401 ARG001 ARG002 ASYNC101 B007 B008 B009 B011 B015 B904 B905 BLE001 C408 C419 C901 D100 D101 D102 D103 D104 D105 D107 D205 D402 D415 D419 DTZ001 DTZ003 DTZ005 DTZ007 E501 E741 EM101 EM102 ERA001 EXE005 F402 F403 F405 F601 F811 F821 F841 FBT001 FBT002 FBT003 FIX002 G001 G002 G004 N801 N802 N805 N806 N816 N999 NPY002 PD901 PERF203 PERF401 PERF402 PIE796 PLE1205 PLR0913 PLR1714 PLR2004 PLW0602 PLW0603 PLW2901 PT004 PT006 PT012 PT015 PTH118 PTH123 PYI024 PYI041 RET503 RET504 RUF001 RUF012 RUF013 S101 S113 S201 S301 S307 S310 S311 S602 S603 S605 S607 S608 SIM103 SIM109 SIM113 SIM115 SIM117 SLF001 SLOT000 T201 T203 TCH003 TD002 TD003 TD004 TRY002 TRY003 TRY300 TRY301 TRY401 W293

from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm, inch
from reportlab.platypus import (
    HRFlowable,
    Image,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


# ruff: noqa: ARG002 A002 DTZ011 C901 T201 ANN001 ANN201 ERA001 D101 D102 D107 E501 PLR2004 BLE001 DTZ005 N802
class CustomerReport:
    def __init__(self, filename, data) -> None:
        self.data = data
        self.filename = filename
        self.pdf = SimpleDocTemplate(self.filename, pagesize=A4)
        self.table = Table(data)
        self.rowNumb = self.get_rowNumb()

        style = TableStyle([
            ('BACKGROUND', (0, 0), (3, 0), colors.lightgrey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 4),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ])

        self.table.setStyle(style)

        self.print_report()

    def get_rowNumb(self):
        return len(self.data)

    def print_report(self):
        try:
            elems = [self.table]
            self.pdf.build(elems)
        except Exception as e:
            return 'error', e
        return 'success', None


class ProductsReport:
    def __init__(self, filename, data, title) -> None:
        self.data = data
        self.filename = filename
        self.pdf = SimpleDocTemplate(self.filename, pagesize=A4)
        self.table = Table(data)
        self.title = title
        self.paragraph_style = ParagraphStyle(
            name='Centered',
            alignment=TA_CENTER,
            fontSize=14,
            leading=16,
        )
        self.table_style = TableStyle([
            ('BACKGROUND', (0, 0), (4, 0), colors.lightgrey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 4),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ])

    def get_date_time(self):
        now = datetime.now()
        date = now.strftime('%d/%m/%Y')
        time = now.strftime('%H:%M:%S')
        return f'({date} - {time})'

    def print_report(self):
        try:
            story = [Paragraph(self.title, self.paragraph_style)]
            story.append(Paragraph(self.get_date_time(), self.paragraph_style))
            story.append(Spacer(1, 0.5 * inch))

            self.table.setStyle(self.table_style)
            story.append(self.table)

            self.pdf.build(story)
        except Exception as e:
            return 'error', e
        return 'success', self.filename


class SaleReport:
    # filename

    # header_data = [
    #     'Empresa XYZ',
    #     'Rua ABC, 123',
    #     '(99) 9999-9999',
    #     'empresa@xyz.com'
    # ]

    # sale_data = [
    #     '001',
    #     '26/06/2023'
    # ]

    # customer_data = [
    #     'Cliente A',
    #     '123.456.789-00',
    #     '(88) 8888-8888',
    #     'cliente@cliente.com',
    #     'Rua Cliente, 456'
    # ]

    # products_data = [[], [], [], ...] list of lists

    def __init__(
        self,
        kwargs,
    ) -> None:
        """Init it.

        filename: Path,
        header_data: map,
        sale_data: map,
        customer_data: map,
        products_data: map,
        """
        self.filename = kwargs.get('filename')
        self.header_data = kwargs.get('header_data')
        self.sale_data = kwargs.get('sale_data')
        self.customer_data = kwargs.get('customer_data')
        self.products_data = kwargs.get('products_data')
        self.pdf = None
        self.numb_pages = int

    def get_header_data(self):
        # Cabeçalho com o logo e os dados da empresa
        logo = Image(r'C:\logo.png', 50, 50)

        header_table = Table([
            [logo, '', self.header_data[0]],
            ['', '', self.header_data[1]],
            ['', '', f'{self.header_data[2]} - {self.header_data[3]}'],
        ])

        header_table.setStyle(
            TableStyle([
                ('FONTNAME', (2, 0), (2, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (2, 0), (2, 0), 14),
                ('FONTNAME', (2, 1), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (2, 1), (-1, -1), 12),
                ('LEFTPADDING', (0, 0), (-1, -1), 0),
                ('TOPPADDING', (0, 0), (-1, -1), 0),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
                ('SPAN', (0, 0), (1, 2)),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ]),
        )

        return header_table

    def get_sale_data(self):
        # Número do pedido e data
        sale_table = Table([
            [
                f'Pedido número: {self.sale_data[0]} - Data: {self.sale_data[1]}',
            ],
        ])
        sale_table.setStyle(
            TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 13),
                ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ]),
        )
        return sale_table

    def get_customer_data(self):
        # Dados do cliente
        customer_table = Table([
            [
                f'Cliente: {self.customer_data[0]} - CPF: {self.customer_data[1]}',
            ],
            [
                f'Tel.: {self.customer_data[2]} - E-mail: {self.customer_data[3]}',
            ],
            [self.customer_data[4]],
        ])
        customer_table.setStyle(
            TableStyle([
                ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 0), (-1, -1), 12),
                ('LEFTPADDING', (0, 0), (-1, -1), 0),
                ('TOPPADDING', (0, 0), (-1, -1), 0),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ]),
        )
        return customer_table

    def get_products_table_data(self, products_data):
        # Dados dos produtos
        products_table = []
        products_table.append([
            'CÓD. PROD.',
            'DESCRIÇÃO',
            'MARCA',
            'QUANT',
            'V. UNIT.',
            'V. Total',
        ])

        for products in products_data:
            products_table = products[:]
        table = Table(products_table)

        style = TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ])
        if products_data[-1][4] == 'Total:':
            style.add('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold')
            style.add('BACKGROUND', (0, -1), (-1, -1), colors.lightgrey)

        table.setStyle(style)
        return table

    def draw_footer(self, canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica', 8)
        canvas.drawRightString(
            A4[0] - cm,
            cm,
            'Página %d de %d' % (doc.page, self.numb_pages),
        )
        canvas.restoreState()

    def create_pdf(self):
        try:
            self.pdf = SimpleDocTemplate(
                self.filename,
                pagesize=A4,
                leftMargin=1 * cm,
                rightMargin=1 * cm,
                topMargin=1 * cm,
                bottomMargin=1 * cm,
            )

            story = []
            max_items_per_page = 25
            num_items = len(self.products_data)
            self.numb_pages = num_items // max_items_per_page + (
                num_items % max_items_per_page > 0
            )

            line = HRFlowable(
                width='100%',
                thickness=1,
                lineCap='round',
                color=colors.black,
            )
            dotted_line = HRFlowable(
                width='100%',
                thickness=1,
                lineCap='round',
                color=colors.black,
                dash=(2, 2),
            )

            for page in range(self.numb_pages):
                story.extend((
                    line,
                    Spacer(1, 0.5 * cm),
                    self.get_header_data(),
                    Spacer(1, 0.5 * cm),
                    line,
                    Spacer(1, 0.5 * cm),
                    self.get_sale_data(),
                    self.get_customer_data(),
                    Spacer(1, 0.5 * cm),
                ))

                inicio = page * max_items_per_page
                fim = min((page + 1) * max_items_per_page, num_items)
                story.append(
                    self.get_products_table_data(
                        self.products_data[inicio:fim],
                    ),
                )

                if page < self.numb_pages - 1:
                    story.extend((
                        Spacer(1, 0.5 * cm),
                        dotted_line,
                        PageBreak(),
                    ))

            story.extend((Spacer(1, 0.5 * cm), line))
            self.pdf.build(
                story,
                onFirstPage=self.draw_footer,
                onLaterPages=self.draw_footer,
            )
        except Exception as e:
            return 'error', e
        return 'success', None
