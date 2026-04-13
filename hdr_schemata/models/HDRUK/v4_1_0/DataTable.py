from __future__ import annotations

from typing import Optional, List

from pydantic import BaseModel, Field, constr

from hdr_schemata.definitions.HDRUK import *
from hdr_schemata.models.HDRUK.v3_0_0.annotations import annotations

from hdr_schemata.models.HDRUK.v3_0_0.DataColumn import DataColumn

an = annotations.structuralMetadata.tables


class DataTable(BaseModel):
    class Config:
        extra = "forbid"

    name: Optional[constr(min_length=1, max_length=500)] = Field(
        None, **an.name.__dict__
    )
    description: Optional[constr(min_length=1, max_length=20000)] = Field(
        None, **an.description.__dict__
    )
    size: Optional[int] = Field(
        None,
        title="Table size",
        description="Number of Complete Entries.",
        json_schema_extra={
            "guidance": (
                "Provides a measure of the completeness of the data set. A row which includes "
                "n/a against columns that are not relevant or not applicable should still be "
                "counted as complete."
            )
        },
    )
    columns: List[DataColumn] = Field(
        ..., title=an.columns._title, description=an.columns._description
    )
