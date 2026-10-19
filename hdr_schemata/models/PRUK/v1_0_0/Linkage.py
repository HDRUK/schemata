from typing import Optional
from pydantic import Field
from hdr_schemata.models.HDRUK.v3_0_0.DatasetDescriptor import DatasetDescriptor
from hdr_schemata.models.HDRUK.v3_0_0.EnrichmentAndLinkage import (
    EnrichmentAndLinkage as BaseLinkage,
)

from .annotations import annotations

an = annotations.linkage

class Linkage(BaseLinkage):
    waveOf: Optional[DatasetDescriptor] = Field(
        None, **an.waveOf.__dict__, json_schema_extra={"guidance": an.waveOf.guidance}
    )
