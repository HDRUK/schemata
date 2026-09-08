from pydantic import Field
from hdr_schemata.definitions.HDRUK import *

from typing import Optional

from .FormatAndStandards import FormatAndStandards

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
