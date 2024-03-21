from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .DatasetLinkage import DatasetLinkage

from .annotations import annotations

an = annotations.linkage


class Linkage(BaseModel):
    class Config:
        extra = "forbid"

    # note: this is a new field
    #      what are we going to do with it?
    isGeneratedUsing: Optional[CommaSeparatedValues] = Field(
        None, **an.isGeneratedUsing.__dict__
    )

    # note: may need to be commad separated list of URLs?
    associatedMedia: Optional[CommaSeparatedValues] = Field(
        None, **an.associatedMedia.__dict__
    )

    # note: new field - what are we going to do with it??
    dataUses: Optional[CommaSeparatedValues] = Field(None, **an.dataUses.__dict__)

    # note: dont we have this already somewhere else? Linked DOIs?
    isReferenceIn: Optional[CommaSeparatedValues] = Field(
        None, **an.isReferenceIn.__dict__
    )

    # note: limit this is comma separated values of URLs?
    tools: Optional[CommaSeparatedValues] = Field(None, **an.tools.__dict__)

    datasetLinkage: Optional[DatasetLinkage] = Field(None, **an.datasetLinkage.__dict__)

    # note: something wrong with this description and/or something needs updating with what this is needed for...
    investigations: Optional[CommaSeparatedValues] = Field(
        None, **an.investigations.__dict__
    )
