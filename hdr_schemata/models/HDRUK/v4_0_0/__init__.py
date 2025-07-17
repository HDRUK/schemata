from hdr_schemata.models.HDRUK.v3_0_0 import Hdruk300
import json
from typing import Optional, List
from pydantic import Field

from .Provenance import Provenance
from .Revision import Revision

from .annotations import annotations as an
from .Summary import Summary

class Hdruk400(Hdruk300):

    provenance: Optional[Provenance] = Field(
        None, description=an.provenance.description, title=an.provenance.title
    )

    revisions: List[Revision] = Field(
        ..., description=an.revisions.description, title=an.revisions.title
    )

    summary: Summary = Field(
        ..., description=an.summary._description, title=an.summary._title
    )

    @classmethod
    def save_schema(cls, location="./4.0.0/schema.json"):
        with open(location, "w") as f:
            json.dump(cls.model_json_schema(), f, indent=6)
