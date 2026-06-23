from typing import Optional

from pydantic import BaseModel, Field

from hdr_schemata.models.HDRUK.v3_0_0.FormatAndStandards import FormatAndStandards
from hdr_schemata.models.HDRUK.v3_0_0.Usage import Usage
from hdr_schemata.models.HDRUK.v3_0_0 import Hdruk300
from hdr_schemata.models.HDRUK.v3_0_0.annotations import annotations

from .Access import Access

an = annotations.accessibility


class Accessibility(BaseModel):
    class Config:
        extra = "forbid"

    usage: Optional[Usage] = Field(
        None, title=an.usage.title, description=an.usage.description
    )

    access: Access = Field(..., description=an.description, title=an.title)

    formatAndStandards: Optional[FormatAndStandards] = Field(
        None,
        title=an.formatAndStandards.title,
        description=an.formatAndStandards.description,
    )
