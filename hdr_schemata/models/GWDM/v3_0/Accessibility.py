from typing import Optional

from pydantic import BaseModel, Field

from hdr_schemata.models.GWDM.v2_0.annotations import annotations as v20_an

from .Access import Access
from .FormatAndStandards import FormatAndStandards
from .Usage import Usage

an = v20_an.accessibility


class Accessibility(BaseModel):
    class Config:
        extra = "forbid"

    usage: Optional[Usage] = Field(
        None, title=an.usage.title, description=an.usage.description
    )
    access: Access = Field(
        ..., title=an.access.title, description=an.access.description
    )
    formatAndStandards: Optional[FormatAndStandards] = Field(
        None,
        title="Format and Standards",
        description="Format and standards information for the dataset.",
    )
