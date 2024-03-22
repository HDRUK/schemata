from pydantic import Field
from hdr_schemata.definitions.HDRUK import *

from hdr_schemata.models.GWDM.v1_1 import Accessibility as BaseAccessibility
from .Access import Access

from .annotations import annotations

an = annotations.accessibility


class Accessibility(BaseAccessibility):
    access: Access = Field(
        ..., description=an.access.description, title=an.access.title
    )
