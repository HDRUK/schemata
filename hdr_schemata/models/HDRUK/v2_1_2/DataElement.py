from typing import Optional
from pydantic import BaseModel, Field, constr
from hdr_schemata.definitions.HDRUK import *

from hdr_schemata.annotations import annotations

an = annotations.HDRUK.v2p1p2.dataElement


class DataElement(BaseModel):
    class Config:
        extra = "allow"

    name: Name = Field(..., **an.name.__dict__)
    dataType: str = Field(..., **an.dataType.__dict__)
    description: Optional[constr(min_length=1, max_length=20000)] = Field(
        None, **an.description.__dict__
    )
    sensitive: bool = Field(..., **an.sensitive.__dict__)
