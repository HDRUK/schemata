from typing import Optional, List
from pydantic import Field
from hdr_schemata.models.HDRUK.v2_2_0 import (
    EnrichmentAndLinkage as BaseEnrichmentAndLinkage,
)

from hdr_schemata.definitions.HDRUK import Url

from .annotations import annotations

an = annotations.enrichmentAndLinkage


class EnrichmentAndLinkage(BaseEnrichmentAndLinkage):
    syntheticDataWebLink: Optional[List[Url]] = Field(
        None, **an.syntheticDataWebLink.__dict__
    )
