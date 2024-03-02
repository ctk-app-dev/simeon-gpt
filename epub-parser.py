import json
from bs4 import BeautifulSoup
from collections import defaultdict
from pathlib import Path


def parse_xhtml(path):
    base_path = Path(__file__).parent  # this will make sure it works regardless of OS/cwd
    html_doc = open(f"{base_path}/{path}", "r")

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Assuming 'html_doc' is your xhtml document
    soup = BeautifulSoup(html_doc, "lxml")

    texts = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

    # Finding all the h4 elements
    h4_elements = soup.find_all('h4')
    for h in h4_elements:
        outermost_layer = h.text.replace('\xa0', ' ').title()
        current_day = 'Sunday'  # Reset to default at the start of each new section, if necessary

        next_element = h.find_next_siblings()
        for sibling in next_element: 
            if sibling.name == 'h4':
                break  # Stop if the next h4 is reached

            ## TODO This is the code that needs refactoring. Instead of treating each paragraph as a distinct unit to operate on.
            ## TODO I want to treat each tag BETWEEN morning/evening as a distinct unit. That will allow me to account for years.
            ## * If you do not have Better Comments, get it.
            text = sibling.get_text().strip()

            # Update the current day based on the italic text
            italic_text = sibling.find('i')
            if italic_text:
                day_of_week = italic_text.get_text().strip()
                if any(day in day_of_week for day in weekdays):
                    current_day = day_of_week  

            # Append the text to the current section and day in the dictionary
            text_to_list = text.split('\n')
            daytime = [text.strip() for text in text_to_list if any(keyword in text.lower() for keyword in ['evening', 'morning'])]
            for time in daytime:
                innermost_layer = [item.strip() for item in text_to_list 
                                   if not any(day in item for day in weekdays) 
                                   and item not in daytime]
                texts[outermost_layer][current_day][time].extend(innermost_layer)

    return texts


file = open('files_to_scrape.txt', 'r').read().splitlines()

for i in file:
    texts = parse_xhtml(i)
    title = i.split('/')[-1].split('.')[0]
    with open(f'assets/{title}.json', 'w') as f:
        json.dump(texts, f, indent=2)

# print(json.dumps(parse_xhtml('assets/OEBPS/Text/EasterSeason.xhtml'), indent=2))