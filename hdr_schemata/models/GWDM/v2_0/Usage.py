from typing import Optional
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *
from hdr_schemata.definitions.HDRUK.CommaSeparatedValues import CommaSeparatedValuesV2

from .Organisation import Organisation

from .annotations import annotations

an = annotations.accessibility.usage


class Usage(BaseModel):
    class Config:
        extra = "forbid"

    dataUseLimitation: Optional[CommaSeparatedValuesV2] = Field(
        None, **an.dataUseLimitation.__dict__
    )

    dataUseRequirement: Optional[CommaSeparatedValuesV2] = Field(
        None, **an.dataUseRequirements.__dict__
    )

    resourceCreator: Optional[Organisation] = Field(None, **an.resourceCreator.__dict__)
