import requests
import re
from bs4 import BeautifulSoup

res = requests.get("https://www.ukri.org/councils/mrc/facilities-and-resources/find-an-mrc-facility-or-resource/cohort-directory/")
page = res.text

soup = BeautifulSoup(page, 'html.parser')

categories = {}
for li in soup.findAll('li'):
    text = li.get_text()
    if not ":" in text: continue
    name,values = text.split(":")
    if name not in categories:
        categories[name] = []
    categories[name].extend(re.split(',|and',values))

categories = {
    name : list(set([v.lstrip() for v in values]))
    for name,values in categories.items()
}
    
print (categories)
