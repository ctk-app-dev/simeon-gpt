import json
import xml.etree.ElementTree as ET
from ebooklib import epub

def extract_toc_items(epub_path):
    # Load the EPUB file
    book = epub.read_epub(epub_path)

    # Extract the table of contents
    toc = book.get_item_with_id('ncx')

    # If the TOC is found, parse its content
    if toc:
        # Parse the XML content
        root = ET.fromstring(toc.content)

        # Define the namespace (common for EPUB NCX files)
        namespaces = {'ncx': 'http://www.daisy.org/z3986/2005/ncx/'}

        # Extract each navPoint (TOC item)
        toc_items = []
        for nav_point in root.findall('.//ncx:navPoint', namespaces):
            nav_label = nav_point.find('ncx:navLabel/ncx:text', namespaces).text
            content_src = nav_point.find('ncx:content', namespaces).get('src')
            toc_items.append({'label': nav_label, 'source': content_src})

        return toc_items
    else:
        print("Table of contents not found.")
        return []

# Test the function
epub_path = 'assets/bcp1928.epub'
toc_items = extract_toc_items(epub_path)

# Save the extracted TOC items to a JSON file
with open('toc.json', 'w') as f:
    json.dump(toc_items, f, indent=4)

# Extract content from the EPUB
epub_path = 'assets/bcp1928.epub'

# Save the extracted content to a JSON file
with open('parsed_epub_for_content.json', 'w') as f:
    json.dump(content_dict, f, indent=4)
