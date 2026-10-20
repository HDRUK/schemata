from typing import Optional, Union, List
from pydantic import BaseModel, Field, constr
from hdr_schemata.definitions.HDRUK import *

from .DataTable import DataTable

from .annotations import annotations

an = annotations.structuralMetadata.tables


class StructuralMetadata(BaseModel):
    class Config:
        extra = "forbid"

    tables: Optional[List[DataTable]] = Field(
        None,
        description=an._description,
        title=an._title,
    )

    syntheticDataWebLink: Optional[List[Url]] = Field(
        None, **an.syntheticDataWebLink.__dict__
    )

