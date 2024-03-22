from typing import Optional
from pydantic import Field
from hdr_schemata.definitions.HDRUK import CommaSeparatedValues

from hdr_schemata.models.GWDM.v1_1 import Access as BaseAccess


from .annotations import annotations

an = annotations.accessibility.access


class Access(BaseAccess):
    accessServiceCategory: Optional[CommaSeparatedValues] = Field(
        None, **an.accessServiceCategory.__dict__
    )
