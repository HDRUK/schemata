from hdr_schemata.models.HDRUK.v2_1_3 import Hdruk213
import json
from typing import Optional, List
from pydantic import Field

from hdr_schemata.models.HDRUK.v2_1_3 import *
from .TissuesSampleCollection import TissuesSampleCollection
from .Summary import Summary
from .Coverage import Coverage


class Hdruk220(Hdruk213):
    # update on summary to include datasetType and population size
    summary: Summary = Field(
        ...,
        description="Summary metadata must be completed by Data Custodians onboarding metadata into the Innovation Gateway MVP.",
        title="Summary",
    )

    # overload Coverage with an updated version of it..
    coverage: Optional[Coverage] = Field(
        None,
        description="Observational, Spatial and Temporal coverage",
        title="Coverage",
    )

    tissuesSampleCollection: Optional[List[TissuesSampleCollection]] = Field(
        None,
        description="Metadata collection for Tissue Samples datasets",
        title="Tissues Sample Collection",
    )

    @classmethod
    def save_schema(cls, location="./2.2.0/schema.json"):
        with open(location, "w") as f:
            json.dump(cls.model_json_schema(), f, indent=6)
