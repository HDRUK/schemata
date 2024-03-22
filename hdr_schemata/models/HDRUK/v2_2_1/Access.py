from typing import Optional, List
from pydantic import Field
from hdr_schemata.definitions.HDRUK import AccessService

from hdr_schemata.models.HDRUK.v2_2_0 import Access as BaseAccess


from .annotations import annotations

an = annotations.accessibility.access


class Access(BaseAccess):
    accessServiceCategory: Optional[List[AccessService]] = Field(
        None, **an.accessServiceCategory.__dict__
    )
