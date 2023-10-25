import requests
import json
from bs4 import BeautifulSoup

def remove_leading(text):
    if text.startswith('\n'):
        text = text.lstrip('\n')
    return text


url = 'https://schema.org/Dataset'
url = 'https://schema.org/CreativeWork'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

tables = soup.find_all('table', class_ = 'definition-table')

template = r'''
{name}: {_type} = Field(
     None,
     description="{description}"
)'''

model = []
for table in tables:
    trs = table.find_all('tr')
    for tr in trs[1:]:
        tds = tr.find_all(['th','td'])
        if (len(tds) != 3): continue
        name,_type,description = [x.text.strip() for x in tds]
        filled_template = template.format(name=name, _type=_type, description=description)
        model.append(filled_template)

print ("\n".join(model))
        

#print (json.dumps([s['name'] for s in schema],indent=6))


