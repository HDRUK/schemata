from hdr_schemata.models.HDRUK.v2_1_2 import Hdruk212
import json
from typing import Optional
from pydantic import Field

from hdr_schemata.models.HDRUK.v2_1_2 import *
from .Provenance import Provenance


from .annotations import annotations as an


class Hdruk213(Hdruk212):
    provenance: Optional[Provenance] = Field(
        None, title=an.provenance.title, description=an.provenance.description
    )

    @classmethod
    def save_schema(cls, location="./2.1.3/schema.json"):
        with open(location, "w") as f:
            json.dump(cls.model_json_schema(), f, indent=6)
