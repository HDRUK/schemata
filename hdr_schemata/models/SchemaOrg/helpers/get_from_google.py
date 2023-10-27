import requests
import json
from bs4 import BeautifulSoup

def remove_leading(text):
    if text.startswith('\n'):
        text = text.lstrip('\n')
    return text

url = 'https://developers.google.com/search/docs/appearance/structured-data/dataset'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

tables = soup.find_all('table', class_ = 'responsive')



schema = []
for table in tables:
    trs = table.find_all('tr')
    for tr in trs:
        tds = tr.find_all('td')
        if len(tds) == 2:
            obj =  {
                'name':remove_leading(tds[0].text).rstrip(),
                'type':remove_leading(tds[1].text).split("\n")[0].rstrip()
            }
            schema.append(obj)
             

print (json.dumps([s['name'] for s in schema],indent=6))


