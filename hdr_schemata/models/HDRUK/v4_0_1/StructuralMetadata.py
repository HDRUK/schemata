from __future__ import annotations

from typing import Optional, List

from pydantic import BaseModel, Field

from hdr_schemata.definitions.HDRUK import Url
from hdr_schemata.models.HDRUK.v3_0_0.annotations import annotations

from .DataTable import DataTable

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
