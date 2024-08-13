from typing import Optional, List, Union
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.omics


class Omics(BaseModel):
    class Config:
        extra = "forbid"

    assay: Optional[Assay] = Field(
        ..., 
        **an.assay.__dict__, 
        json_schema_extra={"guidance": an.assay.guidance}
    )

    platform: Optional[Platform] = Field(
        ..., 
        **an.platform.__dict__, 
        json_schema_extra={"guidance": an.platform.guidance}
    )


    
