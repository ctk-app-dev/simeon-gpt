import requests
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTChar, LTTextBox
import json


# Download the PDF
url = "http://justus.anglican.org/resources/bcp/1928Standard/bcp1928std.pdf"
response = requests.get(url)
filename = "assets/bcp1928.pdf"
with open(filename, 'wb') as f:
    f.write(response.content)

# Extract text and styles from the PDF
data = []

for page_layout in extract_pages(filename):
    text_content = []

    for element in page_layout:
        if isinstance(element, LTTextBox):
            for text_line in element:
                for char in text_line:
                    if isinstance(char, LTChar):
                        text_content.append(char.get_text())
                        ncolor = char.graphicstate.ncolor if hasattr(char.graphicstate, 'ncolor') else 'Unknown'

    page_data = {
        "page": page_layout.pageid,
        "text": "".join(text_content),
    }
    data.append(page_data)

# Save to JSON
with open("parsed_pdf_for_page_numbers.json", "w") as f:
    json.dump(data, f, indent=4)

print("Extraction completed!")
