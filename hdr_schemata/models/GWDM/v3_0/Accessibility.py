from typing import Optional

from pydantic import BaseModel, Field

from .Access import Access
from .FormatAndStandards import FormatAndStandards
from .Usage import Usage


class Accessibility(BaseModel):
    class Config:
        extra = "forbid"

    usage: Optional[Usage] = Field(
        None,
        title="Usage",
        description="This section includes information about how the data can be used and how it is currently being used.",
    )
    access: Access = Field(
        ...,
        title="Access",
        description="This section includes information about data access",
    )
    formatAndStandards: Optional[FormatAndStandards] = Field(
        None,
        title="Format and Standards",
        description="Section includes technical attributes for language vocabularies, sizes etc. and gives researchers facts about and processing the underlying data in the dataset.",
    )
