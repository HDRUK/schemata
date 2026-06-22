from __future__ import annotations

import json
from typing import List, Optional

from pydantic import BaseModel, Field

from hdr_schemata.models.GWDM.v2_0 import Gwdm20
from hdr_schemata.models.GWDM.v2_0.DataTable import DataTable
from hdr_schemata.models.GWDM.v2_0.DemographicFrequency import DemographicFrequency
from hdr_schemata.models.GWDM.v2_0.Linkage import Linkage
from hdr_schemata.models.GWDM.v2_0.Observations import Observation
from hdr_schemata.models.GWDM.v2_0.Omics import Omics
from hdr_schemata.models.GWDM.v2_0.Required import Required
from hdr_schemata.models.GWDM.v2_0.TissuesSampleCollection import TissuesSampleCollection
from hdr_schemata.models.GWDM.v2_0.annotations import annotations as v20_an

from .Accessibility import Accessibility
from .Coverage import Coverage
from .Distribution import Distribution
from .Provenance import Provenance
from .QualityAnnotation import QualityAnnotation
from .Summary import Summary

an = v20_an


class Gwdm30(BaseModel):
    class Config:
        extra = "forbid"

    required: Required = Field(
        ..., description=an.required.description, title=an.required.title
    )
    summary: Summary = Field(
        ..., description=an.summary._description, title=an.summary._title
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
    linkage: Optional[Linkage] = Field(
        None, description=an.linkage.description, title=an.linkage.title
    )
    observations: Optional[List[Observation]] = Field(
        None, description=an.observations.description, title=an.observations.title
    )
    structuralMetadata: Optional[List[DataTable]] = Field(
        None,
        description=an.structuralMetadata.description,
        title=an.structuralMetadata.title,
    )
    tissuesSampleCollection: Optional[List[TissuesSampleCollection]] = Field(
        None,
        description=an.tissuesSampleCollection.description,
        title=an.tissuesSampleCollection.title,
    )
    demographicFrequency: Optional[DemographicFrequency] = Field(
        None,
        description=an.demographicFrequency.description,
        title=an.demographicFrequency.title,
    )
    omics: Optional[Omics] = Field(
        None,
        description=an.omics.description,
        title=an.omics.title,
    )
    distributions: Optional[List[Distribution]] = Field(
        None,
        title="Distributions",
        description="DCAT-compliant distribution records for this dataset (dcat:Distribution).",
    )
    qualityAnnotations: Optional[List[QualityAnnotation]] = Field(
        None,
        title="Quality Annotations",
        description="Quality annotation records for this dataset (dqv:QualityAnnotation).",
    )

    @classmethod
    def save_schema(cls, location: str = "./3.0/schema.json") -> None:
        with open(location, "w") as f:
            json.dump(cls.model_json_schema(), f, indent=6)
