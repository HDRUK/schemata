import requests
import json
from bs4 import BeautifulSoup

def remove_leading(text):
    if text.startswith('\n'):
        text = text.lstrip('\n')
    return text


url = 'https://schema.org/Dataset'
url = 'https://schema.org/CreativeWork'
url = 'https://schema.org/PropertyValue'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

tables = soup.find_all('table', class_ = 'definition-table')

template = r'''
{name}: {_type} = Field(
     None,
     description=r{quotes}{description}{quotes}
)'''

model = []
for table in tables[:1]:
    trs = table.find_all('tr')
    for tr in trs[1:]:
        tds = tr.find_all(['th','td'])
        if (len(tds) != 3): continue
        name,_type,description = [x.text.strip() for x in tds]

        if 'or' in _type:
            _types = ', '.join([x.strip() for x in _type.strip().split("or")])
            _type = f'Union[{_types}]'

        _type = _type.replace('URL','AnyURL')

        _type = f'Optional[{_type}]'

        filled_template = template.format(name=name, _type=_type, description=description,quotes="'''")
        model.append(filled_template)

print ("\n".join(model))
        

#print (json.dumps([s['name'] for s in schema],indent=6))


