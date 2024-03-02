import json
from bs4 import BeautifulSoup
from collections import defaultdict
from pathlib import Path

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
base_path = Path(__file__).parent / "assets" / "OEBPS" / "Text" # this will make sure it works regardless of OS/cwd

html_doc = open(f"{base_path}/Trinity.xhtml", "r")

# Assuming 'html_doc' is your xhtml document
soup = BeautifulSoup(html_doc, "lxml")

texts = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

# Finding all the h4 elements
h4_elements = soup.find_all('h4')
for h in h4_elements:
    outermost_layer = h.text.replace('\xa0', ' ').title()
    current_day = 'Sunday'  # Reset to default at the start of each new section, if necessary

    next_element = h.find_next_sibling()
    while next_element and next_element.name != 'h4':
        if next_element.name == 'p':
            text = next_element.get_text().strip()
            italic_text = next_element.find('i')
            if italic_text:
                day_of_week = italic_text.get_text().strip()
                if day_of_week in weekdays:
                    current_day = day_of_week  # Update the current day based on the italic text
            # Append the text to the current section and day in the dictionary
            text_to_list = text.split('\n')
            daytime = [text.strip() for text in text_to_list if any(keyword in text.lower() for keyword in ['evening', 'morning'])]
            for time in daytime:
                innermost_layer = [item.strip() for item in text_to_list if item not in weekdays and item not in daytime]
                texts[outermost_layer][current_day][time].extend(innermost_layer)
            # texts[outermost_layer][current_day].append(daytime)
        next_element = next_element.find_next_sibling()

# 'texts' dictionary now structured by h4 headings and contains all p tags grouped accordingly

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
        q.append(h.next_siblings)
        
    return soup
