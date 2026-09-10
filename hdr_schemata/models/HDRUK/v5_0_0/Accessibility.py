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
        description="Information on the permitted uses, limitations, and attribution requirements for the dataset.",
    )

    access: Access = Field(
        ...,
        title="Access",
        description="Details of how to request and obtain access to the dataset, including rights, costs, and jurisdiction.",
    )

    formatAndStandards: Optional[FormatAndStandards] = Field(
        None,
        title="Format and Standards",
        description="Technical standards and formats used in the dataset, including vocabularies, data models, language, and file formats.",
    )
