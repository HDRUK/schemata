from typing import Optional, List
from pydantic import BaseModel, Field, constr
from hdr_schemata.definitions.HDRUK import *

from .DataValue import DataValue

from .annotations import annotations

an = annotations.structuralMetadata.tables.columns


class DataColumn(BaseModel):

    name: Name = Field(..., **an.name.__dict__)
    dataType: str = Field(
        ...,
        **an.dataType.__dict__,
    )

    description: Optional[constr(min_length=1, max_length=20000)] = Field(
        None,
        **an.description.__dict__,
    )

    sensitive: bool = Field(
        ...,
        **an.sensitive.__dict__,
    )

    values: Optional[List[DataValue]] = Field(
        None, description=an.values._description, title=an.values._title
    )
