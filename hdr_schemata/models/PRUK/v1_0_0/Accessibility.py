from pydantic import Field
from typing import Optional
from hdr_schemata.models._shared.v3.FormatAndStandards import FormatAndStandards
from .Usage import Usage
from .annotations import annotations

an = annotations.accessibility

from hdr_schemata.models._shared.v1.Accessibility import (
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
