from hdr_schemata.models.GWDM.v1_0 import Gwdm10
from pydantic import BaseModel
import pandas as pd
import json
import typing
import enum

def get_fields(structure,model: type[BaseModel]):
    model_hints = typing.get_type_hints(model)
    for name, field in model.model_fields.items():
        if name == 'root':
            continue

        t = field.annotation

        _type = model_hints[name]
        if isinstance(model_hints[name],type):
            _type = model_hints[name].__name__
        else:
            _type = model_hints[name].__args__[0]
            if not isinstance(_type,type):
                _type = _type.__args__[0]
            _type = _type.__name__

        value = {
            'name':name,
            'required':field.is_required(),
            'title':field.title,
            'description':field.description,
            'title':field.title,
            'examples':field.examples,
            'type':_type
        }

        if hasattr(t,'__args__'):
            t = t.__args__[0]
            
        if isinstance(t, type) and issubclass(t, BaseModel):
            subItems = []
            get_fields(subItems,t)
            value['subItems'] = subItems


        structure.append(value)

def json_to_markdown(structure,level=2):
    md = ""
    for field in structure:
        name = field.pop('name')
        subItems = field.pop('subItems',None)            
        description = field.pop('description')

        table = ""
        if not subItems:
            table = pd.Series(field).sort_index().to_frame().T.set_index('title')
            table = table.to_markdown()
        
        heading = "#"*level
        md += rf'''
{heading} {name}

{description}
        
{table}
'''
        if subItems:
            md += json_to_markdown(subItems,level=level+1)

        
    return md

structure = []
get_fields(structure,Gwdm10)

with open('temp.json','w') as f:
    json.dump(structure,f,indent=6)

md = json_to_markdown(structure)
    
with open('temp.md','w') as f:
    f.write(md)



