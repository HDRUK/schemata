from typing import Optional, List
from pydantic import BaseModel, Field, constr
from hdr_schemata.definitions.HDRUK import *

from .DataColumn import DataColumn

from .annotations import annotations

an = annotations.structuralMetadata.tables


class DataTable(BaseModel):
    class Config:
        extra = "forbid"

    name: Optional[constr(min_length=1, max_length=500)] = Field(
        ..., **an.name.__dict__
    )
    description: Optional[constr(min_length=1, max_length=20000)] = Field(
        None, **an.description.__dict__
    )
    columns: List[DataColumn] = Field(
        ..., title=an.columns._title, description=an.columns._description
    )
