import json
import xml.etree.ElementTree as ET
from ebooklib import epub
import bs4

# Open the EPUB file
book = epub.read_epub('assets/bcp1928.epub')

# Access the book's content
for item in book.get_items():
    # Extract the text content from the item
    if item.get_type() == epub.ITEM_DOCUMENT:
        content = item.get_content()
        # Process the content as needed

        # Example: Print the content
        print(content)
# def extract_toc_items(epub_path):
#     # Load the EPUB file
#     book = epub.read_epub(epub_path)

#     # Extract the table of contents
#     toc = book.get_item_with_id('ncx')

#     # If the TOC is found, parse its content
#     if toc:
#         # Parse the XML content
#         root = ET.fromstring(toc.content)

#         # Define the namespace (common for EPUB NCX files)
#         namespaces = {'ncx': 'http://www.daisy.org/z3986/2005/ncx/'}

#         # Extract each navPoint (TOC item)
#         toc_items = []
#         for nav_point in root.findall('.//ncx:navPoint', namespaces):
#             nav_label = nav_point.find('ncx:navLabel/ncx:text', namespaces).text
#             content_src = nav_point.find('ncx:content', namespaces).get('src')
#             toc_items.append({'label': nav_label, 'source': content_src})

#         return toc_items
#     else:
#         print("Table of contents not found.")
#         return []

# # Test the function
# epub_path = 'assets/bcp1928.epub'
# toc_items = extract_toc_items(epub_path)

# # Save the extracted TOC items to a JSON file
# with open('toc.json', 'w') as f:
#     json.dump(toc_items, f, indent=4)

# def extract_content_from_epub(epub_path, toc_items):
#     # Load the EPUB file
#     book = epub.read_epub(epub_path)

#     # Dictionary to store the extracted content
#     content_dict = {}

#     # Extract content for each item in the table of contents
#     for item in toc_items:
#         # Get the EPUB item using the source path
#         epub_item = book.get_item_with_href(item["source"])

#         # If the item is found, store its content
#         if epub_item:
#             content_dict[item["label"]] = epub_item.content.decode('utf-8')
#             # ! Line 54 needs work. Epubs contain too much info
#         else:
#             print(f"Content not found for: {item['label']}")

#     return content_dict

# # Load the table of contents from the JSON
# with open('toc.json', 'r') as f:
#     toc_items = json.load(f)

# # Extract content from the EPUB
# epub_path = 'assets/bcp1928.epub'
# content_dict = extract_content_from_epub(epub_path, toc_items)

# # Save the extracted content to a JSON file
# with open('parsed_epub_for_content.json', 'w') as f:
#     json.dump(content_dict, f, indent=4)
