import json
from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Union
from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

from hdr_schemata.definitions.HDRUK import *

from .Revision import Revision
from .Summary import Summary
from .Documentation import Documentation
from .Coverage import Coverage
from .Provenance import Provenance
from .Accessibility import Accessibility
from .Access import Access
from .EnrichmentAndLinkage import EnrichmentAndLinkage
from .Observations import Observation
from .DataClass import DataClass
from .DataElement import DataElement

from hdr_schemata.annotations import annotations

an = annotations.HDRUK.v2p1p2


class Hdruk212(BaseModel):
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

    structuralMetadata: Optional[List[DataClass]] = Field(
        None,
        description=an.structuralMetadata.description,
        title=an.structuralMetadata.title,
    )

    @classmethod
    def save_schema(cls, location="./2.1.2/schema.json"):
        with open(location, "w") as f:
            json.dump(cls.model_json_schema(), f, indent=6)
