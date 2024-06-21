from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Union
from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

from hdr_schemata.definitions.HDRUK import *

import json

from .Required import Required
from .Summary import Summary
from .Coverage import Coverage
from .Provenance import Provenance
from .Accessibility import Accessibility
from .Linkage import Linkage
from .Observations import Observation
from .DataTable import DataTable
from .TissuesSampleCollection import TissuesSampleCollection

from .Usage import Usage
from .Access import Access


from .annotations import annotations as an


class Gwdm20(BaseModel):

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

    tissuesSampleCollection: Optional[List[TissuesSampleCollection]] = Field(
        None,
        description=an.tissuesSampleCollection.description,
        title=an.tissuesSampleCollection.title,
    )

    @classmethod
    def save_schema(cls, location="./2.0/schema.json"):
        with open(location, "w") as f:
            json.dump(cls.model_json_schema(), f, indent=6)
