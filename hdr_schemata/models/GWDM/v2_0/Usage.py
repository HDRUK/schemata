from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .Organisation import Organisation

from .annotations import annotations

an = annotations.accessibility.usage


class Usage(BaseModel):
    class Config:
        extra = "forbid"

    dataUseLimitation: Optional[CommaSeparatedValues] = Field(
        ..., **an.dataUseLimitation.__dict__
    )

    dataUseRequirement: Optional[CommaSeparatedValues] = Field(
        ..., **an.dataUseRequirements.__dict__
    )

    resourceCreator: Optional[Organisation] = Field(None, **an.resourceCreator.__dict__)
