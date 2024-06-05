from hdr_schemata.models.HDRUK.v2_2_1 import Accessibility as BaseAccessibility
from pydantic import Field
from typing import Optional
from hdr_schemata.definitions.HDRUK import *

from .Access import Access
from .FormatAndStandards import FormatAndStandards
from .Usage import Usage

from .annotations import annotations

an = annotations.accessibility


class Accessibility(BaseAccessibility):

    usage: Optional[Usage] = Field(
        None, title=an.usage.title, description=an.usage.description
    )

    access: Access = Field(..., description=an.description, title=an.title)

    formatAndStandards: Optional[FormatAndStandards] = Field(
        None,
        title=an.formatAndStandards.title,
        description=an.formatAndStandards.description,
    )
