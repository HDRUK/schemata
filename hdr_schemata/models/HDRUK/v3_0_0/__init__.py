from hdr_schemata.models.HDRUK.v2_2_1 import Hdruk221
import json
from typing import Optional, List
from pydantic import Field

from .Accessibility import Accessibility
from .Coverage import Coverage
from .DataClass import DataClass
from .Documentation import Documentation
from .EnrichmentAndLinkage import EnrichmentAndLinkage
from .Observations import Observation
from .Provenance import Provenance
from .Summary import Summary
from .TissuesSampleCollection import TissuesSampleCollection

from .annotations import annotations as an


class Hdruk300(Hdruk221):

    summary: Summary = Field(
        ..., description=an.summary._description, title=an.summary._title
    )

    documentation: Optional[Documentation] = Field(
        None, description=an.documentation._description, title=an.documentation._title
    )

    coverage: Optional[Coverage] = Field(
        None, description=an.coverage.description, title=an.coverage.title
    )

    provenance: Optional[Provenance] = Field(
        None, description=an.provenance.description, title=an.provenance.title
    )

    accessibility: Accessibility = Field(
        ..., description=an.accessibility.description, title=an.accessibility.title
    )

    enrichmentAndLinkage: Optional[EnrichmentAndLinkage] = Field(
        None,
        description=an.enrichmentAndLinkage.description,
        title=an.enrichmentAndLinkage.title,
    )

    observations: List[Observation] = Field(
        ..., description=an.observations.description, title=an.observations.title
    )

    tissuesSampleCollection: Optional[List[TissuesSampleCollection]] = Field(
        None,
        description="Metadata collection for Tissue Samples datasets",
        title="Tissues Sample Collection",
    )

    structuralMetadata: Optional[List[DataClass]] = Field(
        None,
        description=an.structuralMetadata.description,
        title=an.structuralMetadata.title,
    )

    @classmethod
    def save_schema(cls, location="./3.0.0/schema.json"):
        with open(location, "w") as f:
            json.dump(cls.model_json_schema(), f, indent=6)
