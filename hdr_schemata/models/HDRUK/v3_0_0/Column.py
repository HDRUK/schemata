from typing import Optional
from pydantic import BaseModel, Field, constr
from hdr_schemata.definitions.HDRUK import *


class Column(BaseModel):
    class Config:
        extra = "allow"

    name: Name = Field(...)
    description: Optional[constr(min_length=1, max_length=20000)] = Field(...)
    frequency: int = Field(...)
