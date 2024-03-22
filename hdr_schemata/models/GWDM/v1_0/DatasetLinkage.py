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

    # note: this could be greatly improved - link with DataCollections or other Dataset objects?
    isPartOf: Optional[CommaSeparatedValues] = Field(None, **an.isPartOf.__dict__)

    # note: why was this included? Need to ask Damon as it's an 'extra'
    isMemberOf: Optional[CommaSeparatedValues] = Field(None, **an.isMemberOf.__dict__)

    # note: current data is nonsensical...
    #      make better use out of this my linking to urls or gatewayIDs of other datasets?
    linkedDatasets: Optional[CommaSeparatedValues] = Field(
        None, **an.linkedDatasets.__dict__
    )
