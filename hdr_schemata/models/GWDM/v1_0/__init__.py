from hdr_schemata.models.GWDM.base import GwdmBaseModel
import json

class Gwdm10(GwdmBaseModel):
    @classmethod
    def save_schema(cls,location='./1.0/schema.json'):
        with open(location,'w') as f:
            json.dump(cls.model_json_schema(),f,indent=6)
