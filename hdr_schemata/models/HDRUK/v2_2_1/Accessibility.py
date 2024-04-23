from pydantic import Field
from hdr_schemata.definitions.HDRUK import *

from hdr_schemata.models.HDRUK.v2_2_0 import Accessibility as BaseAccessibility

from typing import Optional

from .Access import Access
from .FormatAndStandards import FormatAndStandards

from .annotations import annotations

an = annotations.accessibility


class Accessibility(BaseAccessibility):
    access: Access = Field(..., description=an.description, title=an.title)

      formatAndStandards: Optional[FormatAndStandards] = Field(
        None,
        title=an.formatAndStandards.title,
        description=an.formatAndStandards.description,
    )