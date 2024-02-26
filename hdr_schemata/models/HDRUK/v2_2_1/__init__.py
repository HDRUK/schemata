from hdr_schemata.models.HDRUK.v2_2_0 import Hdruk220
import json
from typing import Optional, List
from pydantic import Field

from .EnrichmentAndLinkage import EnrichmentAndLinkage


class Hdruk221(Hdruk220):

    enrichmentAndLinkage: Optional[EnrichmentAndLinkage] = Field(
        None,
        description="This section includes information about related datasets that may have previously been linked, as well as indicating if there is the opportunity to link to other datasets in the future. If a dataset has been enriched and/or derivations, scores and existing tools are available this section allows providers to indicate this to researchers.",
        title="Enrichment and Linkage",
    )

    @classmethod
    def save_schema(cls, location="./2.2.1/schema.json"):
        with open(location, "w") as f:
            json.dump(cls.model_json_schema(), f, indent=6)
