from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar
from inspect import getmembers

def inspect_page(pdf_path, page_number=0):
    """
    Parse and inspect the structure of a single page in a PDF.

    :param pdf_path: Path to the PDF file.
    :param page_number: Zero-based index of the page to inspect.
    """
    object_types = set()  # Using a set to avoid duplicates

    # Extract pages from the PDF
    pages = extract_pages(pdf_path)

    print(dir(pages))
    for page in pages:
        for obj in page:
            object_types.add(type(obj).__name__)  # Add the type name to the set
    print(list(object_types))
    
# Test the function
pdf_path = "bcp1928.pdf"
inspect_page(pdf_path, page_number=11)
