from typing import Optional
from pydantic import Field

from hdr_schemata.models.GWDM.v2_0.Linkage import Linkage as BaseLinkage

from .DatasetLinkage import DatasetLinkage

from .annotations import annotations

an = annotations.linkage


class Linkage(BaseLinkage):
    datasetLinkage: Optional[DatasetLinkage] = Field(None, **an.datasetLinkage.__dict__)
