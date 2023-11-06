"""Gerar documentos DOCX com python-docx.

https://python-docx.readthedocs.io/en/latest/.
"""
import datetime as dt
import inspect
import logging
import typing
from pathlib import Path

import pytz
from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Pt, RGBColor

texto = """Lorem Ipsum
"Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit..."
"There is no one who loves pain itself, who seeks after it and wants to have it, simply because it is pain..."
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam egestas at felis at accumsan. Etiam id ligula consectetur lacus elementum dignissim. Quisque nibh mi, interdum nec felis quis, vestibulum finibus leo. Fusce tincidunt id dolor et vestibulum. Suspendisse at massa blandit, accumsan ante ac, iaculis diam. Vivamus ultrices lorem ante, ut euismod lectus condimentum ut. Fusce laoreet, arcu nec fringilla venenatis, purus magna vehicula mauris, sit amet sodales arcu purus dignissim arcu. Duis at rhoncus quam. In a tincidunt nunc. Morbi placerat, ex quis ultricies blandit, orci odio elementum neque, at congue dui quam ut risus. Ut sollicitudin porttitor consectetur. Nullam egestas odio id nisi tincidunt, at consectetur tortor cursus. In id aliquet sapien, a molestie lacus. Aliquam ut ullamcorper risus.
Nunc facilisis malesuada turpis, sed ultricies dolor venenatis eu. Cras auctor sit amet nulla accumsan varius. Aenean purus leo, dapibus in odio vel, interdum mattis tortor. Duis tincidunt velit vel orci sollicitudin, et tristique ante commodo. Maecenas quam nibh, dignissim vel sodales eget, dictum ac nisi. Mauris sit amet ligula ullamcorper, maximus ex sed, fringilla urna. Ut porttitor ante vehicula euismod rutrum. Proin sed dignissim ante. Maecenas porta nulla a leo dignissim, in dignissim dolor tincidunt. Pellentesque rutrum pulvinar felis, in aliquam ligula sodales id.
Fusce elementum dolor eget sagittis pulvinar. Donec ipsum neque, fringilla non felis a, faucibus semper ex. Integer eget posuere mauris. Nulla ornare quam vitae velit ultricies bibendum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Phasellus facilisis risus quis urna dignissim malesuada in eu nibh. Sed eu vulputate leo.
Nunc euismod nulla a finibus laoreet. Proin bibendum id leo eget pretium. Nullam porttitor gravida tortor, non egestas ipsum placerat non. Phasellus aliquet fermentum imperdiet. Morbi condimentum massa et sagittis lobortis. Nam vel sagittis mauris. Vestibulum magna orci, finibus ut massa ac, pharetra laoreet erat. Praesent euismod tortor ac enim vehicula consectetur. Etiam imperdiet rutrum consequat. Cras hendrerit hendrerit tincidunt. Curabitur sagittis ut orci vitae volutpat. Proin ultricies malesuada nunc a tincidunt. Proin eleifend nec tellus quis dictum. Curabitur pulvinar ligula ut augue facilisis bibendum sed commodo ipsum.
In iaculis nunc eu lacinia lobortis. Etiam ac gravida ligula. Vestibulum maximus mauris eget urna sodales porta. Duis hendrerit non tellus quis fringilla. Donec id nisi facilisis neque dignissim dignissim vitae at mi. Maecenas bibendum ut odio aliquam sodales. Nulla mattis eu leo vitae imperdiet. Quisque ut volutpat lectus, eu euismod erat. Morbi risus dui, eleifend quis semper quis, ornare ac risus. Nulla varius mollis sapien, sed tempor massa blandit semper. Nam vitae malesuada urna, ac pretium ex. Ut ultricies iaculis purus, vel ullamcorper enim. Ut molestie hendrerit odio, nec placerat lectus mattis ut.
Aliquam faucibus neque dui, nec bibendum dolor posuere nec. Fusce laoreet risus quis ante luctus, quis placerat eros interdum. Donec aliquam est eu tellus egestas sagittis. Nam mauris ligula, vestibulum at metus sed, posuere faucibus urna. Proin nec enim sapien. Sed nec hendrerit odio. Mauris sapien nunc, tempor condimentum mauris eu, suscipit facilisis augue. Mauris sed dui nisl.
Donec hendrerit ex id nisl porta molestie. In euismod vestibulum sem ut ornare. Nulla in dolor vel mauris elementum euismod. Sed at tristique nisi. Cras nec libero eu est efficitur placerat. Nam at augue auctor, lobortis elit non, laoreet massa. Curabitur non cursus nibh. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed rhoncus dapibus sollicitudin. Nam faucibus ligula eu faucibus placerat. In eu ipsum consectetur, fermentum erat quis, vulputate tellus. Vivamus et leo placerat nunc mollis eleifend et ultrices justo.
Praesent dignissim velit et cursus viverra. Maecenas pretium neque massa, vitae feugiat sem sollicitudin non. Maecenas scelerisque imperdiet nulla, et lobortis mauris dapibus a. Donec vitae lorem velit. Cras eu justo dictum odio rhoncus fermentum quis vitae dolor. Nulla id molestie turpis. Etiam at egestas lacus, non congue orci. Nam facilisis, risus at bibendum tristique, lorem enim ullamcorper enim, ac dapibus nibh lacus eu nunc. In condimentum hendrerit nunc quis rutrum. Nunc eu lacus est. Ut mattis turpis quis tellus tempor, quis facilisis lacus efficitur. Aenean eget blandit tellus.
In hac habitasse platea dictumst. Ut sit amet neque felis. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Proin blandit augue vel nisl pulvinar, eu elementum nisl feugiat. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vivamus volutpat egestas vehicula. Vestibulum et tincidunt enim. Maecenas augue enim, luctus vitae sollicitudin at, volutpat ut est. In pretium nisi velit, ac hendrerit dolor interdum sit amet. Donec vehicula scelerisque rhoncus. Cras vitae magna bibendum, elementum felis non, vestibulum arcu. Donec ornare et nisl vel dapibus. Donec id dolor risus. Aliquam elementum tempor ligula sed tempus. Phasellus vel est magna.
Proin odio massa, vestibulum non odio et, faucibus ultrices quam. Duis rutrum quam nec neque sodales finibus. In congue vehicula porta. Phasellus tincidunt ante vel purus porta faucibus. Integer at cursus turpis. Curabitur tempus lobortis magna eu feugiat. Quisque suscipit neque at tellus gravida gravida. Aenean tristique quis ante sed tincidunt. Suspendisse et mattis nunc.
Maecenas nec imperdiet lorem, ut mattis nunc. Duis molestie efficitur ligula, ut dignissim magna pulvinar a. Ut dignissim magna non aliquet viverra. Cras tempus consectetur erat, sit amet vestibulum magna euismod et. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam scelerisque sollicitudin tellus, eu dapibus eros tincidunt a. Ut malesuada molestie risus, sit amet blandit massa tempus a. Maecenas dui ex, commodo sit amet enim at, dictum facilisis elit. Nulla fermentum urna eu est imperdiet accumsan. Duis vel luctus orci, sed pulvinar arcu.
Cras sed lacus non magna venenatis ultricies quis quis purus. Nullam vitae accumsan dolor. Pellentesque aliquam eros nisl, iaculis gravida quam facilisis in. Quisque est nulla, pretium ut nisl nec, luctus tincidunt orci. Sed et sem a velit fringilla rutrum. Vestibulum tincidunt ligula a dolor lacinia ultrices. In euismod faucibus urna. Fusce ornare laoreet eros, nec condimentum nisi. Aenean sed sem vel lacus interdum gravida in nec nisi. Maecenas tincidunt ornare risus eget lobortis. Praesent vel placerat neque. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras fringilla viverra massa, vel commodo elit porta ut. Nam a lacinia nulla, at ultricies justo. Sed velit urna, ornare ut ex eget, pharetra tempus ipsum. Cras scelerisque magna nunc, eu faucibus libero accumsan et.
Morbi rhoncus metus quis odio lacinia sagittis. Quisque scelerisque, ex in ornare accumsan, risus nunc interdum nisi, non pretium nunc nunc posuere metus. Phasellus sit amet est euismod orci blandit tempus. Etiam ac dapibus nibh. Vestibulum elementum eros ut dolor hendrerit scelerisque. Sed id nibh quis mi mattis bibendum in non augue. Maecenas tristique nibh quis pulvinar maximus. Sed placerat felis ante, sit amet tempor turpis congue quis. Fusce eget lacus viverra, tempor sem et, rhoncus nunc. Duis congue nunc vitae lectus rutrum consequat. Sed luctus in enim feugiat suscipit. Donec elementum porttitor erat in ultricies. Phasellus mollis commodo nisi at maximus. Integer in ligula in tellus ultrices sagittis.
Sed quis porttitor ex. Aliquam suscipit massa vitae turpis eleifend pharetra. Suspendisse suscipit viverra ligula vel ultricies. Nulla iaculis, mauris ut elementum gravida, quam augue faucibus lorem, sit amet sollicitudin ex est bibendum lorem. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut ullamcorper nulla eu enim ultrices, eu dapibus lectus fringilla. Sed sagittis mollis nunc, nec tempor urna. Phasellus ipsum purus, volutpat in lorem ac, posuere sagittis quam. Nunc ut posuere eros. Ut libero ante, ullamcorper a posuere ut, tincidunt eget leo. Fusce faucibus facilisis lectus, vitae lacinia nisi aliquam quis.
Nullam molestie, urna eu mattis lobortis, tortor ante venenatis sem, a gravida neque est at nunc. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Donec a lectus nec est ornare laoreet eu eu purus. Cras nec blandit lorem. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nulla in vestibulum ex. Mauris nulla tortor, volutpat aliquam aliquet a, ultricies mattis nulla. Praesent in gravida nulla. Nam finibus, tellus a ultricies volutpat, ipsum nisi dignissim mi, at lobortis tellus tellus sit amet ipsum. Cras sed velit id orci efficitur commodo et vel erat. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Morbi viverra tellus id tortor finibus sollicitudin. Proin sed ligula vel est elementum placerat. Proin sed mauris ut urna placerat finibus. Nunc volutpat lectus sit amet varius tristique.
Generated 15 paragraphs, 1394 words, 9332 bytes of Lorem Ipsum at {}"""


def tratativa1():
    """"""
    documento = Document()
    texto.format(
        pytz.timezone('America/Sao_Paulo')
        .localize(dt.datetime.now())
        .isoformat(),
    )
    documento.add_paragraph(texto)
    documento.save(Path(__file__).parent / f'{inspect.stack()[0][3]}.docx')


def tratativa2():
    """Estilo no DOCX."""
    documento = Document()
    texto = """Olá Mundo!!!"""
    paragraf = documento.add_paragraph(texto)
    paragraf.style = documento.styles.add_style(
        'Mystyle',
        WD_STYLE_TYPE.PARAGRAPH,
    )
    paragraf.style.font.name = 'Algerian'
    paragraf.style.font.size = Pt(15)
    paragraf.style.font.bold = True
    paragraf.style.font.italic = True

    documento.save(Path(__file__).parent / f'{inspect.stack()[0][3]}.docx')


def tratativa3():
    """Estilo no DOCX."""
    documento = Document()
    texto = """Olá Mundo!!!"""
    paragraf = documento.add_paragraph(texto)
    paragraf.style = documento.styles.add_style(
        (mystyle := inspect.stack()[0][3]),
        WD_STYLE_TYPE.PARAGRAPH,
    )
    paragraf.style.font.name = 'Algerian'
    paragraf.style.font.size = Pt(15)
    paragraf.style.font.bold = True
    paragraf.style.font.italic = True
    paragraf.style.font.underline = True
    paragraf.style.font.color.rgb = RGBColor(255, 0, 0)

    # sem estilo aplicado
    documento.add_paragraph('Novo paragrafo.')

    # com estilo previamente criado
    documento.add_paragraph('Novo paragrafo.', mystyle)

    documento.save(Path(__file__).parent / f'{mystyle}.docx')


def tratativa4():
    """Exibir estilos disponiveis."""
    documento = Document()
    for estilo in documento.styles:
        print(estilo)


def tratativa5():
    """Utilizar estilos pré-existentes."""
    documento = Document()

    documento.add_paragraph('Cabeçalho', 'Header')
    documento.add_paragraph('Primeiro paragrafo.', 'Heading 1')
    documento.add_paragraph('Segundo paragrafo.')
    documento.add_paragraph('Terceiro paragrafo.')
    documento.add_paragraph('Quarto paragrafo.')

    documento.save(Path(__file__).parent / f'{inspect.stack()[0][3]}.docx')


def tratativa6():
    """Criar um documento a partir de uma configuração de estilo preexistente em outro arquivo."""
    documento = Document(Path(__file__).parent / 'tratativa2.docx')
    documento.add_paragraph('Cabeçalho', 'Heading 1')
    documento.add_paragraph('Primeiro paragrafo.', 'Mystyle')
    documento.add_paragraph('Segundo paragrafo.', 'Mystyle')
    documento.add_paragraph('Terceiro paragrafo.', 'Mystyle')
    documento.add_paragraph('Quarto paragrafo.', 'Mystyle')

    documento.save(Path(__file__).parent / f'{inspect.stack()[0][3]}.docx')


def tratativa7():
    """Formatação Negrito em texto."""
    documento = Document()
    paragraf = documento.add_paragraph('Texto gerado em ')
    paragraf.add_run(
        f"{pytz.timezone('America/Sao_Paulo').localize(dt.datetime.now()).isoformat()} ",
    ).bold = True
    paragraf.add_run('através do ')
    paragraf.add_run('Python').italic = True

    documento.save(Path(__file__).parent / f'{inspect.stack()[0][3]}.docx')


def tratativa8():
    """Quebra de página."""
    documento = Document()

    documento.add_paragraph('Título', 'Heading 1')

    paragraf = documento.add_paragraph('Texto gerado em ')
    paragraf.add_run(
        f"{pytz.timezone('America/Sao_Paulo').localize(dt.datetime.now()).isoformat()} ",
    ).bold = True
    paragraf.add_run('através do ')
    paragraf.add_run('Python').italic = True

    documento.add_page_break()
    documento.add_paragraph('Título', 'Heading 1')
    documento.add_paragraph('Primeiro paragrafo.')
    documento.add_paragraph('Segundo paragrafo.')
    documento.add_paragraph('Terceiro paragrafo.')
    documento.add_paragraph('Quarto paragrafo.')

    documento.save(Path(__file__).parent / f'{inspect.stack()[0][3]}.docx')


def tratativa9():
    """Controle de margem e seções de página."""
    documento = Document()
    for section in documento.sections:
        section.top_margin = Cm(0.5)
        section.bottom_margin = Cm(0.5)
        section.left_margin = Cm(2.5)
        section.right_margin = Cm(0.5)

    paragraf = documento.add_paragraph('Texto gerado em ')
    paragraf.add_run(
        f"{pytz.timezone('America/Sao_Paulo').localize(dt.datetime.now()).isoformat()} ",
    ).bold = True
    paragraf.add_run('através do ')
    paragraf.add_run('Python').italic = True

    documento.save(Path(__file__).parent / f'{inspect.stack()[0][3]}.docx')


def tratativa10():
    """Controle de margem e seções de página."""
    documento = Document()
    for section in documento.sections:
        section.top_margin = Cm(0.5)
        section.bottom_margin = Cm(0.5)
        section.left_margin = Cm(2.5)
        section.right_margin = Cm(0.5)

    paragraf = documento.add_paragraph(texto)
    paragraf.add_run('\nTexto gerado em ')
    paragraf.add_run(
        f"{pytz.timezone('America/Sao_Paulo').localize(dt.datetime.now()).isoformat()} ",
    ).bold = True
    paragraf.add_run('através do ')
    paragraf.add_run('Python').italic = True
    paragraf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    documento.save(Path(__file__).parent / f'{inspect.stack()[0][3]}.docx')


def tratativa11():
    """Imagem."""
    documento = Document()
    content = texto.split('\n')
    logging.debug(content)
    documento.add_paragraph(content.pop(0), 'Heading 1')
    documento.add_paragraph(content.pop(0))
    documento.add_paragraph(content.pop(0))

    documento.add_picture(
        Path(__file__).parent.joinpath('imagem.png').as_posix(),
    )
    documento.add_paragraph(content.pop(0))

    documento.save(Path(__file__).parent / f'{inspect.stack()[0][3]}.docx')


def tratativa12():
    """Imagem."""
    documento = Document()
    content = texto.split('\n')
    documento.add_paragraph(content.pop(0), 'Heading 1')
    documento.add_paragraph(content.pop(0))
    documento.add_paragraph(content.pop(0))

    documento.add_picture(
        Path(__file__).parent.joinpath('imagem.png').as_posix(),
        width=Cm(4),
        height=Cm(4),
    )
    documento.add_paragraph(content.pop(0))

    documento.save(Path(__file__).parent / f'{inspect.stack()[0][3]}.docx')


def tratativa13():
    """Imagem."""
    documento = Document()
    content = texto.split('\n')
    documento.add_paragraph(content.pop(0), 'Heading 1')
    documento.add_paragraph(content.pop(0))
    documento.add_paragraph(content.pop(0))

    image = documento.add_picture(
        Path(__file__).parent.joinpath('imagem.png').as_posix(),
        width=Cm(4),
        height=Cm(4),
    )
    image.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for cont in content:
        parag = documento.add_paragraph(cont)
        parag.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    documento.save(Path(__file__).parent / f'{inspect.stack()[0][3]}.docx')


def tratativa14():
    """Tabela."""
    documento = Document()
    paragrafos = texto.format(
        pytz.timezone('America/Sao_Paulo')
        .localize(dt.datetime.now())
        .isoformat(),
    ).split('\n')

    documento.add_paragraph(paragrafos.pop(0), 'Heading 1')

    for parag in paragrafos[:2]:
        paragraf = documento.add_paragraph(parag)
        paragraf.alignment = WD_ALIGN_PARAGRAPH.CENTER
        paragrafos.pop(0)

    image = documento.add_picture(
        Path(__file__).parent.joinpath('imagem.png').as_posix(),
        width=Cm(4),
        height=Cm(4),
    )
    image.alignment = WD_ALIGN_PARAGRAPH.CENTER

    for cont in paragrafos[:5]:
        parag = documento.add_paragraph(cont)
        parag.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        paragrafos.pop(0)
    records = (
        (3, '101', 'Spam'),
        (7, '422', 'Eggs'),
        (4, '631', 'Spam, spam, eggs, and spam'),
    )

    table = documento.add_table(rows=1, cols=3)
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Qty'
    hdr_cells[1].text = 'Id'
    hdr_cells[2].text = 'Desc'
    for qty, id, desc in records:
        row_cells = table.add_row().cells
        row_cells[0].text = str(qty)
        row_cells[1].text = id
        row_cells[2].text = desc

    for cont in paragrafos:
        parag = documento.add_paragraph(cont)
        parag.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    documento.save(Path(__file__).parent / f'{inspect.stack()[0][3]}.docx')


def tratativa15():
    """Tabela: Estilos disponíveis."""
    documento = Document()
    for estilo in (x for x in documento.styles):
        print(estilo)


def tratativa16():
    """Tabela."""
    documento = Document()
    paragrafos = texto.format(
        pytz.timezone('America/Sao_Paulo')
        .localize(dt.datetime.now())
        .isoformat(),
    ).split('\n')

    documento.add_paragraph(paragrafos.pop(0), 'Heading 1')

    for parag in paragrafos[:2]:
        paragraf = documento.add_paragraph(parag)
        paragraf.alignment = WD_ALIGN_PARAGRAPH.CENTER
        paragrafos.pop(0)

    image = documento.add_picture(
        Path(__file__).parent.joinpath('imagem.png').as_posix(),
        width=Cm(4),
        height=Cm(4),
    )
    image.alignment = WD_ALIGN_PARAGRAPH.CENTER

    for cont in paragrafos[:5]:
        parag = documento.add_paragraph(cont)
        parag.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        paragrafos.pop(0)
    records = (
        (3, '101', 'Spam'),
        (7, '422', 'Eggs'),
        (4, '631', 'Spam, spam, eggs, and spam'),
    )

    table = documento.add_table(rows=1, cols=3, style='Light List Accent 1')
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Qty'
    hdr_cells[1].text = 'Id'
    hdr_cells[2].text = 'Desc'
    for qty, id, desc in records:
        row_cells = table.add_row().cells
        row_cells[0].text = str(qty)
        row_cells[1].text = id
        row_cells[2].text = desc

    for cont in paragrafos:
        parag = documento.add_paragraph(cont)
        parag.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    documento.save(Path(__file__).parent / f'{inspect.stack()[0][3]}.docx')


def tratativa17():
    """Mala direta MSWord via Python."""
    contrato = Document(Path(__file__).parent / 'Contrato.docx')

    nome = 'Lira da Hashtag'
    item1 = 'Serviço de Treinamento em Excel'
    item2 = 'Apostila Completa de Excel'
    item3 = 'Serviço de Treinamentos de Python'

    {
        'XXXX': nome,
        'YYYY': item1,
        'ZZZZ': item2,
        'WWWW': item3,
        'DD': str(dt.datetime.now().day),
        'MM': str(dt.datetime.now().month),
        'AAAA': str(dt.datetime.now().year),
    }
    for paragraf in contrato.paragraphs:
        print(paragraf)
        if 'XXXX' in paragraf.text:
            paragraf.text = paragraf.text.replace('XXXX', nome)

    contrato.save(Path(__file__).parent / f'{inspect.stack()[0][3]}.docx')


def tratativa18():
    """Mala direta MSWord via Python."""
    contrato = Document('Contrato.docx')

    nome = 'Lira da Hashtag'
    item1 = 'Serviço de Treinamento em Excel'
    item2 = 'Apostila Completa de Excel'
    item3 = 'Serviço de Treinamentos de Python'

    dicionario_valores = {
        'XXXX': nome,
        'YYYY': item1,
        'ZZZZ': item2,
        'WWWW': item3,
        'DD': str(dt.datetime.now().day),
        'MM': str(dt.datetime.now().month),
        'AAAA': str(dt.datetime.now().year),
    }
    for paragraf in contrato.paragraphs:
        for key in dicionario_valores:
            if key in paragraf.text:
                logging.debug(paragraf, key)
                paragraf.text = paragraf.text.replace(
                    key,
                    dicionario_valores.get(key),
                )

    contrato.save(Path(__file__).parent / f'{inspect.stack()[0][3]}.docx')


def run():
    """Running it."""
    functions: list[typing.Callable] = [
        value
        for key, value in globals().items()
        if key.__contains__('tratativa')
    ]
    for func in functions:
        logging.debug(f'{type(func)} {func.__name__}')
        print(f'--- {func.__name__} ---')
        print(f'    >>> {func.__doc__}')
        try:
            if result := func():
                print(result)
        except (TypeError, ValueError) as e:
            logging.error(f'{e.__class__.__name__}: {e}')
        finally:
            logging.debug(f'{func.__name__} finalizada.')
        print('------\n')


if __name__ == '__main__':  # pragma: no cover
    run()
