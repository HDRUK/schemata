from typing import Optional
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .Usage import Usage
from .Access import Access
from .FormatAndStandards import FormatAndStandards


class Accessibility(BaseModel):
    class Config:
        extra = "forbid"

    usage: Optional[Usage] = Field(
        None,
        description="This section includes information about how the data can be used and how it is currently being used",
        title="Usage",
    )
    access: Access = Field(
        ...,
        description="This section includes information about data access",
        title="Access",
    )
    formatAndStandards: Optional[FormatAndStandards] = Field(
        None,
        description="Section includes technical attributes for language vocabularies, sizes etc. and gives researchers facts about and processing the underlying data in the dataset.",
        title="Format and Standards",
    )
