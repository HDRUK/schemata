from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *
from .annotations import annotations

an = annotations.accessibility.usage


class Usage(BaseModel):
    class Config:
        extra = "forbid"

    dataUseLimitation: Optional[List[DataUseLimitationV2]
    ] = Field(
        None, **an.dataUseLimitation.__dict__, json_schema_extra={"guidance": an.dataUseLimitation.guidance}
    )

    dataUseRequirements: Optional[List[DataUseRequirementsV2]
    ] = Field(
        None, **an.dataUseRequirements.__dict__, json_schema_extra={"guidance": an.dataUseRequirements.guidance}
    )

    resourceCreator: Optional[
        Union[Optional[ShortDescription], List[Optional[ShortDescription]]]
    ] = Field(
        None, **an.resourceCreator.__dict__, json_schema_extra={"guidance": an.resourceCreator.guidance}
    )
