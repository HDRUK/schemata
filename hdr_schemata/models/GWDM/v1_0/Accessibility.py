from typing import Optional
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .Usage import Usage
from .Access import Access
from .FormatAndStandards import FormatAndStandards


from hdr_schemata.annotations import annotations

an = annotations.GWDM.v1p0.accessibility


class Accessibility(BaseModel):
    class Config:
        extra = "forbid"

    usage: Optional[Usage] = Field(None, **an.usage.__dict__)
    access: Access = Field(..., **an.access.__dict__)
    formatAndStandards: Optional[FormatAndStandards] = Field(
        None, **an.formatAndStandards.__dict__
    )
