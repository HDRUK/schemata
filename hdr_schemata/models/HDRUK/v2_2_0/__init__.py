from hdr_schemata.models.HDRUK.v2_1_3 import Hdruk213
import json
from typing import Optional
from pydantic import Field

from .TissuesSampleCollection import TissuesSampleCollection
from .Coverage import Coverage


class Hdruk220(Hdruk213):
    tissuesSampleCollection: Optional[TissuesSampleCollection] = Field(
        None,
        description="Metadata collection for Tissue Samples datasets",
        title="Tissues Sample Collection",
    )

    # overload Coverage with an updated version of it..
    coverage: Optional[Coverage] = Field(
        None,
        description="Observational, Spatial and Temporal coverage",
        title="Coverage",
    )

    @classmethod
    def save_schema(cls, location="./2.2.0/schema.json"):
        with open(location, "w") as f:
            json.dump(cls.model_json_schema(), f, indent=6)
