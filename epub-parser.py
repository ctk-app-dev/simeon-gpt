import json
from bs4 import BeautifulSoup
from collections import defaultdict
from pathlib import Path


base_path = Path(__file__).parent / "assets" / "OEBPS" / "Text" # this will make sure it works regardless of OS/cwd

html_doc = open(f"{base_path}/Trinity.xhtml", "r")

# Assuming 'html_doc' is your xhtml document
soup = BeautifulSoup(html_doc, 'lxml')

texts = defaultdict(list)

# Finding all the h4 elements
h4 = soup.find_all('h4')
for h in h4:  # this gets which trinity it is
    q = h.text.replace('\xa0', ' ').title()
    for sibling in h.next_siblings:  # this gets the texts and days of week
        if sibling.name == "p":  # Filtering by  'p' for paragraphs
            texts[q].append((sibling.get_text()))
        else:
            # Handle non-tag siblings (like NavigableString, which could be just text or whitespace) if needed
            pass

# Converting to a regular dict for readability
print(json.dumps(texts, indent=2))

