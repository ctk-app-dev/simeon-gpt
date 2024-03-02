import json
from bs4 import BeautifulSoup
from collections import defaultdict
from pathlib import Path


def parse_xhtml(path):
    base_path = Path(__file__).parent  # this will make sure it works regardless of OS/cwd
    html_doc = open(f"{base_path}/{path}", "r")

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Eve', 'Even']

    # Assuming 'html_doc' is your xhtml document
    soup = BeautifulSoup(html_doc, "lxml")

    texts = defaultdict(lambda: defaultdict(lambda: defaultdict(list))) # so we can do {day: {section: [text]}}

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
                if any(day.lower() in day_of_week.lower() for day in weekdays):
                    current_day = day_of_week  

            # Append the text to the current section and day in the dictionary
            text_to_list = text.split('\n')
            daytime = [text.strip() for text in text_to_list if any(keyword in text.lower() for keyword in ['evening', 'morning', 'eve'])]
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
    with open(f'assets/db/json/{title}.json', 'w') as f:
        json.dump(texts, f, indent=2)

# print(json.dumps(parse_xhtml('assets/OEBPS/Text/EasterSeason.xhtml'), indent=2))
        
# Missing:
#! - The problem on top of all of these is that multiple year options aren't included
# - Correct logic for the first sunday after christmas (those are labeled by dates and not weekdays)
# - missing special notes about † On January 13, read Isa. 60:10. It also doesn't like the † character and puts it as \u00e2\u20ac
# - Epiphany season is dates, not days of week, again
# - Fixed holy days is just a mess with eves and dates. Each section has "eve" and then the date (e.g., december 21) italicized, and then morning and evening
    # - These also have a zillion footnotes
# - Ash Wednesday is treated as a sunday (because it's presented that way, but still)
# - Easter 6, the weekdays are shortened for God knows why
# - Good Friday is treated as a Sunday
        
#* Fixed ish:
#* - trinity eve - now treated as a separate day from saturday
#* - Epiphany eve
#* - Easter Even is there, but it's duplicated the morning readings
#* - I don't understand how the ember days are optional, or where they're supposed to go. Left intentionally blank for now