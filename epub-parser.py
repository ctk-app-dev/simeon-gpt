import json
from bs4 import BeautifulSoup
from collections import defaultdict

base_path = "c:/Users/Ben/simeon-gpt/assets/OEBPS/Text"

html_doc = open(f"{base_path}/Trinity.xhtml", "r")

# Assuming 'html_doc' is your xhtml document
soup = BeautifulSoup(html_doc, 'html.parser')

# Step 1: Find all elements with class `smallcaps` and save their text.
smallcaps_elements = soup.find_all(class_="smallcaps")
smallcaps_text = [element.get_text() for element in smallcaps_elements]

# Step 2: For each `smallcaps` element, find the following <p> elements.
# Since <p> elements are not technically children of <span>, but siblings of <span> or <span>'s parent,
# we'll adjust the strategy to get the next siblings of the <span>'s parent (<p>) that are <p> elements.

# Initialize a dictionary to hold the text of <p> elements for each smallcaps entry
smallcaps_following_p = {text: [] for text in smallcaps_text}

for element in smallcaps_elements:
    # The direct parent might not always be a <p>, so we find the parent and then iterate over the next siblings
    parent_element = element.find_parent()
    for sibling in parent_element.find_next_siblings():
        if sibling.name == 'p':
            smallcaps_following_p[element.get_text()].append(sibling.get_text(separator="\n", strip=True))
        else:
            break  # Stop if the next sibling is not a <p> to only get immediate <p> siblings

print("Smallcaps Texts:", smallcaps_text)
print("Following <p> Elements:", smallcaps_following_p)

