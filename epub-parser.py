import json
from bs4 import BeautifulSoup
from collections import defaultdict
from pathlib import Path

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
base_path = Path(__file__).parent / "assets" / "OEBPS" / "Text" # this will make sure it works regardless of OS/cwd

html_doc = open(f"{base_path}/Trinity.xhtml", "r")

# Assuming 'html_doc' is your xhtml document
soup = BeautifulSoup(html_doc, 'lxml')

texts = defaultdict(list)

# Finding all the h4 elements
h4 = soup.find_all('h4')
for h in h4:  # Iterating over elements to determine the trinity
    q = h.text.replace('\xa0', ' ').title()  # Normalizing and formatting the text
    for sibling in h.next_siblings:  # Iterating over sibling elements
        # Skip processing if the sibling is not a paragraph ('p')
        if sibling.name != "p":
            continue
        
        text = sibling.get_text()

        # Append the text to the dictionary only if it contains any of the weekdays
        if any(day in text for day in weekdays):
            texts[q].append(text)
# Converting to a regular dict for readability
print(json.dumps(texts, indent=2))

