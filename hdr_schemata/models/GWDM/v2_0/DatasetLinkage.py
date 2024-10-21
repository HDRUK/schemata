from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .DatasetDescriptor import DatasetDescriptor

from .annotations import annotations

an = annotations.linkage


class DatasetLinkage(BaseModel):
    class Config:
        extra = "forbid"

    derivedFrom: Optional[List[DatasetDescriptor]] = Field(
        None, **an.derivedFrom.__dict__
    )

    isPartOf: Optional[List[DatasetDescriptor]] = Field(
        None, **an.isPartOf.__dict__
    )

    linkableDatasets: Optional[List[DatasetDescriptor]] = Field(
        None, **an.linkableDatasets.__dict__
    )

    similarToDatasets: Optional[List[DatasetDescriptor]] = Field(
        None, **an.similarToDatasets.__dict__
    )
