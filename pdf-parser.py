import requests
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTChar, LTTextBox
import json


# Download the PDF
url = "http://justus.anglican.org/resources/bcp/1928Standard/bcp1928std.pdf"
response = requests.get(url)
filename = "bcp1928.pdf"
with open(filename, 'wb') as f:
    f.write(response.content)

# Extract text and styles from the PDF
data = []

for page_layout in extract_pages(filename):
    text_content = []
    styles = set()

    for element in page_layout:
        if isinstance(element, LTTextBox):
            for text_line in element:
                for char in text_line:
                    if isinstance(char, LTChar):
                        text_content.append(char.get_text())
                        ncolor = char.graphicstate.ncolor if hasattr(char.graphicstate, 'ncolor') else 'Unknown'

                        # Check if the text is red
                        is_red = ncolor == (1, 0, 0)
                        if is_red:
                                styles.add("red")

    page_data = {
        "page": len(data) + 1,
        "text": "".join(text_content),
        "style": list(styles)
    }
    data.append(page_data)

# Save to JSON
with open("output.json", "w") as f:
    json.dump(data, f, indent=4)

print("Extraction completed!")
