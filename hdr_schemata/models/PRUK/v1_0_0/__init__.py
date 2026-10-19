from hdr_schemata.definitions.HDRUK import *
import json
from typing import Optional, List, Union
from pydantic import Field, BaseModel
from datetime import datetime

# Shared-core sections are reused unchanged from pinned HDRUK versions. PRUK is
# composed from them rather than inheriting a whole HDRUK model, so it owns its
# own top-level shape and required fields.
from hdr_schemata.models._shared.v1.Coverage import Coverage
from hdr_schemata.models._shared.v1.DemographicFrequency import DemographicFrequency
from hdr_schemata.models._shared.v1.Documentation import Documentation
from hdr_schemata.models._shared.v1.Observations import Observation
from hdr_schemata.models._shared.v1.Omics import Omics
from hdr_schemata.models._shared.v1.StructuralMetadata import StructuralMetadata
from hdr_schemata.models._shared.v2.Provenance import Provenance
from hdr_schemata.models._shared.v2.Revision import Revision
from hdr_schemata.models._shared.v2.Summary import Summary

from .Accessibility import Accessibility
from .Linkage import Linkage
from .Population import Population

from .annotations import annotations as an


class Pruk100(BaseModel):
    class Config:
        extra = "forbid"

    identifier: Union[Uuidv4, Optional[Url]] = Field(..., **an.identifier.__dict__)
    version: Semver = Field(..., **an.version.__dict__)
    revisions: Optional[List[Revision]] = Field(
        None, description=an.revisions.description, title=an.revisions.title
    )
    issued: datetime = Field(..., **an.issued.__dict__)
    modified: datetime = Field(..., **an.modified.__dict__)

    summary: Summary = Field(
        ..., description=an.summary._description, title=an.summary._title
    )

    population: Population = Field(
        ..., description=an.population.description, title=an.population.title
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

    linkage: Optional[Linkage] = Field(
        None, description=an.linkage.description, title=an.linkage.title
    )

    observations: Optional[List[Observation]] = Field(
        None, description=an.observations.description, title=an.observations.title
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
    def save_schema(cls, location="./1.0.0/schema.json"):
        with open(location, "w") as f:
            json.dump(cls.model_json_schema(), f, indent=6)
