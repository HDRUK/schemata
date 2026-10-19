from pydantic import Field
from typing import Optional
from hdr_schemata.models.HDRUK.v4_1_0.FormatAndStandards import FormatAndStandards
from .Usage import Usage
from .annotations import annotations

an = annotations.accessibility

from hdr_schemata.models.HDRUK.v3_0_0.Accessibility import (
    Accessibility as BaseAccessibility,
)

class Accessibility(BaseAccessibility):
    formatAndStandards: Optional[FormatAndStandards] = Field(
        None,
        title=an.formatAndStandards.title,
        description=an.formatAndStandards.description,
    )

    usage: Optional[Usage] = Field(
        None, title=an.usage.title, description=an.usage.description
    )
