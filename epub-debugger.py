import json
from bs4 import BeautifulSoup
from collections import defaultdict
from pathlib import Path
import difflib

def debug_epub(path):
    base_path = Path(__file__).parent  # this will make sure it works regardless of OS/cwd
    html_doc = open(f"{base_path}/{path}", "r")

    title_only = path.split('/')[-1].split('.')[0]

    # Assuming 'html_doc' is your xhtml document
    soup = BeautifulSoup(html_doc, "lxml")

    html_text = soup.get_text()

    file_path = './assets/' + title_only + '.json'
    with open(file_path, 'r') as f:
        json_text = f.readlines()

    

    diff = list(difflib.unified_diff(html_text, json_text, fromfile='html', tofile='json'))

    return ''.join(diff)

# print(debug_epub('assets/OEBPS/Text/Trinity.xhtml'))

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_of_week = "Monday"  # Example: "Monday"

# Checking if day_of_week is exactly in weekdays or as a substring of any weekday
if any(day in day_of_week for day in weekdays):
    # Your logic here
    print(f"{day_of_week} is a weekday or contains a weekday name.")
