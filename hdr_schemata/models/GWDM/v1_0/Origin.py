from typing import Optional, List, Union
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *


from .annotations import annotations

an = annotations.provenance.origin


class Origin(BaseModel):
    class Config:
        extra = "forbid"

    # note: shall we update to limit to: https://github.com/HDRUK/schemata-2/blob/master/hdr_schemata/definitions/HDRUK/Purpose.py
    purpose: Optional[CommaSeparatedValues] = Field(None, **an.purpose.__dict__)

    # note: update to limit to: https://github.com/HDRUK/schemata-2/blob/master/hdr_schemata/definitions/HDRUK/Source.py
    source: Optional[CommaSeparatedValues] = Field(None, **an.source.__dict__)

    # note: update to limit to: https://github.com/HDRUK/schemata-2/blob/master/hdr_schemata/definitions/HDRUK/Setting.py
    collectionSituation: Optional[CommaSeparatedValues] = Field(
        None, **an.collectionSituation.__dict__
    )
