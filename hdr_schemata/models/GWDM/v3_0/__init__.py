from __future__ import annotations

import json
from typing import List, Optional

from pydantic import BaseModel, Field

from .Accessibility import Accessibility
from .Coverage import Coverage
from .DatasetFilter import DatasetFilter
from .DataTable import DataTable
from .DemographicFrequency import DemographicFrequency
from .Distribution import Distribution
from .Image import Image
from .Linkage import Linkage
from .Observations import Observation
from .Omics import Omics
from .ProjectGrant import ProjectGrant
from .Provenance import Provenance
from .QualityAnnotation import QualityAnnotation
from .Required import Required
from .Summary import Summary
from .TissuesSampleCollection import TissuesSampleCollection


class Gwdm30(BaseModel):
    class Config:
        extra = "forbid"

    required: Required = Field(
        ...,
        title="Required",
        description="Required metadata needed for the GWDM",
    )
    summary: Summary = Field(
        ...,
        title="Summary",
        description="Summary of metadata describing key pieces of information.",
    )
    coverage: Optional[Coverage] = Field(
        None,
        title="Coverage",
        description="This information includes attributes for geographical and temporal coverage, cohort details etc. to enable a deeper understanding of the dataset content so that researchers can make decisions about the relevance of the underlying data.",
    )
    provenance: Optional[Provenance] = Field(
        None,
        title="Provenance",
        description="Provenance information allows researchers to understand data within the context of its origins and can be an indicator of quality, authenticity and timeliness.",
    )
    accessibility: Accessibility = Field(
        ...,
        title="Accessibility",
        description="Accessibility information allows researchers to understand access, usage, limitations, formats, standards and linkage or interoperability with toolsets.",
    )
    linkage: Optional[Linkage] = Field(
        None,
        title="Linkage",
        description="Metadata for various linkages with datasets and other gateway entities",
    )
    observations: Optional[List[Observation]] = Field(
        None,
        title="Observations",
        description="This section provides an overview of observations of your dataset linked to specific points in time. Multiple observations about the dataset are encouraged to be provided, including multiple observations of the same property at different timepoints. At least one observation is required.",
    )
    structuralMetadata: Optional[List[DataTable]] = Field(
        None,
        title="Structural metadata",
        description="Descriptions of all tables and data elements that can be included in the dataset.",
    )
    tissuesSampleCollection: Optional[List[TissuesSampleCollection]] = Field(
        None,
        title="Tissue Sample Collection",
        description="metedata for tissue samples",
    )
    demographicFrequency: Optional[DemographicFrequency] = Field(
        None,
        title="Demographic frequency",
        description="An object containing demographic frequency data categorised by age, ethnicity, and disease attributes.",
    )
    omics: Optional[Omics] = Field(
        None,
        title="Omics",
        description="Omics",
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
    icons: Optional[List[str]] = Field(
        None,
        title="Icons",
        description="Calculated categorization icons added during export.",
    )
    projectGrants: Optional[List[ProjectGrant]] = Field(
        None, title="Associated Project Grants"
    )
    datasetFilters: Optional[List[DatasetFilter]] = Field(
        None,
        description="Categorization tags regarding cancer type, data type, and access.",
    )
    erd: Optional[Image] = Field(
        None,
        title="Entity Relationship Diagram",
        description="Visual representation of data table relationships.",
        json_schema_extra={
            "guidance": (
                "Please upload an image file (max 5MB) showing the relationship between the different tables"
            )
        },
    )

    @classmethod
    def save_schema(cls, location: str = "./3.0/schema.json") -> None:
        with open(location, "w") as f:
            json.dump(cls.model_json_schema(), f, indent=6)
