from typing import Optional, List, Union
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.provenance.origin


class Origin(BaseModel):
    class Config:
        extra = "forbid"

    purpose: Optional[List[Purpose]] = Field(None, **an.purpose.__dict__)
    source: Optional[Union[Optional[CommaSeparatedValues], List[Source]]] = Field(
        None, **an.source.__dict__
    )
    collectionSituation: Optional[
        Union[Optional[CommaSeparatedValues], List[Setting]]
    ] = Field(None, **an.collectionSituation.__dict__)
