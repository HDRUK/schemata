from typing import Optional, List
from pydantic import Field
from hdr_schemata.models.HDRUK.v2_2_0 import (
    EnrichmentAndLinkage as BaseEnrichmentAndLinkage,
)

from hdr_schemata.definitions.HDRUK import Url


class EnrichmentAndLinkage(BaseEnrichmentAndLinkage):
    syntheticDataWebLink: Optional[List[Url]] = Field(
        None,
        description="Links to locations of information and or raw downloads of synthetic data associated with this dataset",
        example="",
        title="Synthetic Data Web Links",
    )
