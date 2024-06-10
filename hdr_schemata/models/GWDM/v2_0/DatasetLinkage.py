from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.linkage


class DatasetLinkage(BaseModel):
    class Config:
        extra = "forbid"

    isDerivedFrom: Optional[CommaSeparatedValues] = Field(
        None, **an.isDerivedFrom.__dict__
    )

    isPartOf: Optional[CommaSeparatedValues] = Field(None, **an.isPartOf.__dict__)

    isMemberOf: Optional[CommaSeparatedValues] = Field(None, **an.isMemberOf.__dict__)

    linkedDatasets: Optional[CommaSeparatedValues] = Field(
        None, **an.linkedDatasets.__dict__
    )
