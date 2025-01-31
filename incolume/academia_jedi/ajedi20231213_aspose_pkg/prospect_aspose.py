import aspose.words as aw
from tempfile import NamedTemporaryFile
from pathlib import Path

def new_filename(**kwargs) -> Path:
    """Name file.
    
    mode='w+b',
    buffering=-1, 
    encoding=None, 
    newline=None, 
    suffix=None, 
    prefix=None, 
    dir=None, 
    delete=True,
    """
    result = Path(NamedTemporaryFile(**kwargs).name)
    return result


def example1(output_file: Path = "output.docx") -> bool:
    """Exemple oficial.

    aspose-words em https://pypi.org/project/aspose-words/
    """
    # Create a blank document.
    doc = aw.Document()

    # Use a document builder to add content to the document.
    builder = aw.DocumentBuilder(doc)
    # Write a new paragraph in the document with the text "Hello World!".
    builder.writeln("Hello, World!")

    # Save the document in DOCX format. Save format is automatically determined from the file extension.
    doc.save(output_file)


def example2(filein: Path, fileout: Path):
    """Example2."""
    # Load the document from the disc.
    doc = aw.Document(filein)

    # Save the document to HTML format.
    doc.save(fileout)



def run() -> None:
    """Run it."""
    # example1()
    pdfin = Path(__file__).parents[3]/'./data_files/pdf/Illustrator.pdf'
    example2(filein='output.docx', fileout='output.html')
    example2(filein=pdfin.as_posix(), fileout='output2.html')
    example2(filein=pdfin.as_posix(), fileout='output2.docx')

if __name__ == "__main__":
    run()
