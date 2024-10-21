from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .DatasetDescriptor import DatasetDescriptor

from .annotations import annotations

an = annotations.linkage


class DatasetLinkage(BaseModel):
    class Config:
        extra = "forbid"

    isDerivedFrom: Optional[List[DatasetDescriptor]] = Field(
        None, **an.isDerivedFrom.__dict__
    )

    isPartOf: Optional[List[DatasetDescriptor]] = Field(
        None, **an.isPartOf.__dict__
    )

    linkedDatasets: Optional[List[DatasetDescriptor]] = Field(
        None, **an.linkedDatasets.__dict__
    )

    isMemberOf: Optional[List[DatasetDescriptor]] = Field(
        None, **an.isMemberOf.__dict__
    )
