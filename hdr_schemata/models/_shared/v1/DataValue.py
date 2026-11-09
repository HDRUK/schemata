from typing import Optional
from pydantic import BaseModel, Field, constr
from hdr_schemata.definitions.HDRUK import *


from .annotations import annotations

an = annotations.structuralMetadata.tables.columns.values


class DataValue(BaseModel):

    name: Name = Field(..., **an.name.__dict__)

    description: Optional[constr(min_length=1, max_length=20000)] = Field(
        None, **an.description.__dict__
    )

    frequency: Optional[int] = Field(None, **an.frequency.__dict__)
