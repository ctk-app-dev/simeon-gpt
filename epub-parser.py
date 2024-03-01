import json
from bs4 import BeautifulSoup
from collections import defaultdict
from pathlib import Path

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
base_path = Path(__file__).parent / "assets" / "OEBPS" / "Text" # this will make sure it works regardless of OS/cwd

html_doc = open(f"{base_path}/Trinity.xhtml", "r")

# Assuming 'html_doc' is your xhtml document
soup = BeautifulSoup(html_doc, "lxml")

texts = defaultdict(list)

# Finding all the h4 elements
h4 = soup.find_all('h4')
for h in h4:  # Iterating over elements to determine the trinity
    q = h.text.replace('\xa0', ' ').title()
    # Pseudocode:
    # for each heading, get all the sibling 'p' elements until you hit another heading.
    # that should be its own function.

    # then, once you have the xhtml for each week, you can perform other logic; another function
    for sibling in h.next_siblings:
        # Skip processing if the sibling is not a paragraph ('p')
        if sibling.name != "p":
            continue
        
        text = sibling.get_text()

        # Append the text to the dictionary only if it contains any of the weekdays
        if any(day in text for day in weekdays):
            texts[q].append(text.split('Ps.')[0].strip().replace('\n', ' '))
# Converting to a regular dict for readability
print(json.dumps(texts, indent=2))



def get_each_week_xhtml(xhtml_path):
    base_path = Path(__file__).parent / "assets" / "OEBPS" / "Text" # code works regardless of OS/cwd
    html_doc = open(f"{base_path}/{xhtml_path}", "r")
    soup = BeautifulSoup(html_doc, "lxml")

    # Finding all the h4 elements
    h4 = soup.find_all('h4')
    for h in h4:  # Iterating over elements to determine the trinity
        q = h.text.replace('\xa0', ' ').title()
        
    return soup
