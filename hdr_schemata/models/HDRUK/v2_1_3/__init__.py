from hdr_schemata.models.HDRUK.v2_1_2 import Hdruk212
import json


class Hdruk213(Hdruk212):
    @classmethod
    def save_schema(cls, location="./2.1.3/schema.json"):
        with open(location, "w") as f:
            json.dump(cls.model_json_schema(), f, indent=6)
