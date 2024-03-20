from typing import Optional, List
from pydantic import BaseModel, Field, constr
from hdr_schemata.definitions.HDRUK import *

from .DataElement import DataElement

from .annotations import annotations

an = annotations.dataClass


class DataClass(BaseModel):
    class Config:
        extra = "forbid"

    name: Optional[constr(min_length=1, max_length=500)] = Field(
        ..., **an.name.__dict__
    )
    description: Optional[constr(min_length=1, max_length=20000)] = Field(
        None, **an.name.__dict__
    )
    elements: List[DataElement] = Field(..., **an.name.__dict__)
