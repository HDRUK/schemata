from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Union
from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

from hdr_schemata.definitions.HDRUK import *
from hdr_schemata.annotations import annotations

import json

from .Required import Required
from .Summary import Summary
from .Coverage import Coverage
from .Provenance import Provenance
from .Accessibility import Accessibility
from .Linkage import Linkage
from .Observations import Observation
from .DataTable import DataTable

from .Usage import Usage
from .Access import Access

an = annotations.GWDM


class Gwdm10(BaseModel):

    class Config:
        extra = "forbid"

    required: Required = Field(
        ..., description=an.required.description, title=an.required.title
    )

    summary: Summary = Field(
        ..., description=an.summary.description, title=an.summary.title
    )

    coverage: Optional[Coverage] = Field(
        None, description=an.coverage.description, title=an.coverage.title
    )

    provenance: Optional[Provenance] = Field(
        None, description=an.provenance.description, title=an.provenance.title
    )

    accessibility: Accessibility = Field(
        None, description=an.accessibility.description, title=an.accessibility.title
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

    @classmethod
    def save_schema(cls, location="./1.0/schema.json"):
        with open(location, "w") as f:
            json.dump(cls.model_json_schema(), f, indent=6)
