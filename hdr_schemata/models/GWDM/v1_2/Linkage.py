from typing import Optional
from hdr_schemata.models.GWDM.v1_1 import Linkage as BaseLinkage
from pydantic import Field
from hdr_schemata.definitions.HDRUK import CommaSeparatedValues

from .annotations import annotations

an = annotations.linkage


class Linkage(BaseLinkage):
    syntheticDataWebLink: Optional[CommaSeparatedValues] = Field(
        None, **an.syntheticDataWebLink.__dict__
    )
