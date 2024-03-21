from typing import Optional
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .Usage import Usage
from .Access import Access
from .FormatAndStandards import FormatAndStandards

from .annotations import annotations

an = annotations.accessibility


class Accessibility(BaseModel):
    class Config:
        extra = "forbid"

    usage: Optional[Usage] = Field(None, title=an.usage.title)
    access: Access = Field(..., title=an.access.title)
    formatAndStandards: Optional[FormatAndStandards] = Field(
        None, title=an.formatAndStandards.title
    )
