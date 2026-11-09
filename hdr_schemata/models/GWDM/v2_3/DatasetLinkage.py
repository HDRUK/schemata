from typing import Optional, List
from pydantic import Field

from hdr_schemata.models.GWDM.v2_0.DatasetDescriptor import DatasetDescriptor
from hdr_schemata.models.GWDM.v2_0.DatasetLinkage import (
    DatasetLinkage as BaseDatasetLinkage,
)

from .annotations import annotations

an = annotations.linkage


class DatasetLinkage(BaseDatasetLinkage):
    waveOf: Optional[List[DatasetDescriptor]] = Field(
        None, **an.waveOf.__dict__
    )
