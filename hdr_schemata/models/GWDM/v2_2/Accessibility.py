from pydantic import Field
from hdr_schemata.definitions.HDRUK import *

from typing import Optional

from .Usage import Usage

from .annotations import annotations

an = annotations.accessibility

from hdr_schemata.models.GWDM.v2_0.Accessibility import (
    Accessibility as BaseAccessibility,
)


class Accessibility(BaseAccessibility):
    usage: Optional[Usage] = Field(
        None, title=an.usage.title, description=an.usage.description
    )
