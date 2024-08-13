from hdr_schemata.definitions.HDRUK import *
import json
from typing import Optional, List, Union
from pydantic import Field, BaseModel
from datetime import date, datetime

from .Accessibility import Accessibility
from .Coverage import Coverage
from .DemographicFrequency import DemographicFrequency
from .Documentation import Documentation
from .EnrichmentAndLinkage import EnrichmentAndLinkage
from .Observations import Observation
from .Omics import Omics
from .Provenance import Provenance
from .Revision import Revision
from .StructuralMetadata import StructuralMetadata
from .Summary import Summary

from .annotations import annotations as an

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../utils")))
from markdown_cleaner import clean_markdown_from_json


class Hdruk300(BaseModel):
    class Config:
        extra = "forbid"

    identifier: Union[Uuidv4, Optional[Url]] = Field(..., **an.identifier.__dict__)
    version: Semver = Field(..., **an.version.__dict__)
    revisions: List[Revision] = Field(
        ..., description=an.revisions.description, title=an.revisions.title
    )
    issued: datetime = Field(..., **an.issued.__dict__)
    modified: datetime = Field(..., **an.modified.__dict__)

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

    structuralMetadata: Optional[StructuralMetadata] = Field(
        None,
        description=an.structuralMetadata.description,
        title=an.structuralMetadata.title,
    )

    demographicFrequency: Optional[DemographicFrequency] = Field(
        None,
        description=an.demographicFrequency.description,
        title=an.demographicFrequency.title
    )

    omics: Optional[Omics] = Field(
        None,
        description=an.omics.description,
        title=an.omics.title
    )

    @classmethod
    def save_schema(cls, location="./3.0.0/schema.json"):
        with open(location, "w") as f:
            json.dump(clean_markdown_from_json(cls.model_json_schema()), f, indent=6)
