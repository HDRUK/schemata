from pydantic import Field
from hdr_schemata.definitions.HDRUK import *

from hdr_schemata.models.HDRUK.v2_2_0 import Accessibility as BaseAccessibility
from .Access import Access

from .annotations import annotations

an = annotations.accessibility


class Accessibility(BaseAccessibility):
    access: Access = Field(..., description=an.description, title=an.title)
