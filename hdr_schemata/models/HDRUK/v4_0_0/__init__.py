from hdr_schemata.models.HDRUK.v3_0_0 import Hdruk300
import json
from typing import Optional, List
from pydantic import Field

from .Provenance import Provenance

from .annotations import annotations as an


class Hdruk400(Hdruk300):

    provenance: Optional[Provenance] = Field(
        None, description=an.provenance.description, title=an.provenance.title
    )

    @classmethod
    def save_schema(cls, location="./4.0.0/schema.json"):
        with open(location, "w") as f:
            json.dump(cls.model_json_schema(), f, indent=6)
