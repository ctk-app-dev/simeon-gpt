import json
from bs4 import BeautifulSoup
from collections import defaultdict

base_path = "c:/simeon-gpt/assets/OEBPS/Text"

html_doc = open(f"{base_path}/Trinity.xhtml", "r")

# Assuming 'html_doc' is your xhtml document
soup = BeautifulSoup(html_doc, 'html.parser')

# Finding all the h4 elements
h4 = soup.find_all('h4')
for h in h4: # this gets which trinity it is
    print(h.text)
    for sibling in h.next_siblings: # this gets the texts and days of week
        print(sibling)
