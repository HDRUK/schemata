from __future__ import annotations

import json
from typing import List, Optional

from pydantic import BaseModel, Field

from hdr_schemata.models.GWDM.v2_0 import Gwdm20
from hdr_schemata.models.CRUK.v1_0_0 import (
    DatasetFilter as CrukDatasetFilter,
    ProjectGrant as CrukProjectGrant,
)
from hdr_schemata.definitions.HDRUK import Description

from .Summary import Summary


DatasetFilter = CrukDatasetFilter


class Image(BaseModel):
    class Config:
        extra = "forbid"

    image: Optional[str] = Field(
        None,
        title="Image",
        description="An image file.",
        json_schema_extra={
            "contentMediaType": "image/*",
            "guidance": "Upload an image file (PNG, JPG, SVG) Max file size: 5MB.",
        },
    )
    description: Optional[Description] = Field(None)


ProjectGrant = CrukProjectGrant


class Gwdm21(Gwdm20):
    summary: Summary = Field(..., description="Summary of metadata describing key pieces of information.")
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
    def save_schema(cls, location: str = "./2.1/schema.json") -> None:
        with open(location, "w") as f:
            json.dump(cls.model_json_schema(), f, indent=6)
