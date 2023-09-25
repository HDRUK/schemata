from hdr_schemata.models.HDRUK.base import HdrukBaseModel
import json

class Hdruk212(HdrukBaseModel):
    @classmethod
    def save_schema(cls,location='./2.1.2/schema.json'):
        with open(location,'w') as f:
            json.dump(cls.model_json_schema(),f,indent=6)
