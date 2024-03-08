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

from .Usage import Usage
from .Access import Access


class Gwdm10(BaseModel):
    class Config:
        extra = "forbid"

    required: Required = Field(
        ..., description="required metadata needed for the GWDM", title="Required"
    )

    summary: Summary = Field(
        ...,
        description="Summary of metadata describing key pieces of information.",
        title="Summary",
    )

    coverage: Optional[Coverage] = Field(
        None,
        description="Spatial and Temporal coverage",
        title="Coverage",
    )

    provenance: Optional[Provenance] = Field(
        None,
        description="Provenance information",
        title="Provenance",
    )

    accessibility: Accessibility = Field(
        None,
        description="Accessibility information.",
        title="Accessibility",
    )

    linkage: Optional[Linkage] = Field(
        None,
        description="Linkage and enrichment.",
        title="Linkage",
    )

    observations: Optional[List[Observation]] = Field(
        None,
        description="Obsservations",
        title="Observations",
    )
    structuralMetadata: Optional[List[DataTable]] = Field(
        None,
        description="Descriptions of all tables and data elements that can be included in the dataset",
        title="Structural Metadata",
    )

    @classmethod
    def save_schema(cls, location="./1.0/schema.json"):
        with open(location, "w") as f:
            json.dump(cls.model_json_schema(), f, indent=6)
