import json
from bs4 import BeautifulSoup
from collections import defaultdict
from pathlib import Path


base_path = Path(__file__).parent / "assets" / "OEBPS" / "Text" # this will make sure it works regardless of OS/cwd

html_doc = open(f"{base_path}/Trinity.xhtml", "r")

# Assuming 'html_doc' is your xhtml document
soup = BeautifulSoup(html_doc, 'html.parser')

# Finding all the h4 elements
h4 = soup.find_all('h4')
for h in h4: # this gets which trinity it is
    print(h.text)
    for sibling in h.next_siblings: # this gets the texts and days of week
        print(sibling)
