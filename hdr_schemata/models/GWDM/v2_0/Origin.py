from typing import Optional, List, Union
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *


from .annotations import annotations

an = annotations.provenance.origin


class Origin(BaseModel):
    class Config:
        extra = "forbid"

    purpose: Optional[CommaSeparatedValues] = Field(None, **an.purpose.__dict__)

    source: Optional[CommaSeparatedValues] = Field(None, **an.source.__dict__)

    collectionSituation: Optional[CommaSeparatedValues] = Field(
        None, **an.collectionSituation.__dict__
    )

    imageContrast: Optional[Ternary] = Field("Not stated", **an.imageContrast.__dict__)
