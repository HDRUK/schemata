from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.documentation


class Documentation(BaseModel):
    class Config:
        extra = "forbid"

    description: Description = Field(
        None, **an.description.__dict__, json_schema_extra={"guidance": an.description.guidance}
    )

    associatedMedia: Optional[
        Union[Optional[CommaSeparatedValues], List[Optional[Url]]]
    ] = Field(None, **an.associatedMedia.__dict__, json_schema_extra={"guidance": an.associatedMedia.guidance})

    inPipeline: Optional[Pipeline] = Field(
        "Not available", **an.inPipeline.__dict__, json_schema_extra={"guidance": an.inPipeline.guidance}
    )

