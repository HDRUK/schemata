from hdr_schemata.models.SchemaOrg.GoogleRecommended import Dataset as D1
from hdr_schemata.models.SchemaOrg.BioSchema import Dataset as D2
from hdr_schemata.models.SchemaOrg.base import Dataset as D3
import json

location='GoogleRecommended/schema.json'
with open(location,'w') as f:
    json.dump(D1.model_json_schema(),f,indent=6)

location='BioSchema/schema.json'
with open(location,'w') as f:
    json.dump(D2.model_json_schema(),f,indent=6)

location='default/schema.json'
with open(location,'w') as f:
    json.dump(D3.model_json_schema(),f,indent=6)
