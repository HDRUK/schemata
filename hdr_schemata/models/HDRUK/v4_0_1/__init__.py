from __future__ import annotations

import json
from typing import Optional

from pydantic import Field

from hdr_schemata.models.HDRUK.v4_0_0 import Hdruk400
from hdr_schemata.models.HDRUK.v4_0_0.annotations import annotations as an
from hdr_schemata.models.HDRUK.v3_0_0.annotations import annotations as an_v3

from .DatasetFilters import DatasetFilters
from .Icons import Icons
from .Image import Image
from .Project import Project
from .Summary import Summary
from .StructuralMetadata import StructuralMetadata


class Hdruk401(Hdruk400):
    icons: Optional[Icons] = Field(
        None,
        title="Icons",
        description="Calculated categorization icons added during export.",
    )
    summary: Summary = Field(
        ..., description=an.summary._description, title=an.summary._title
    )

    structuralMetadata: Optional[StructuralMetadata] = Field(
        None,
        description=an_v3.structuralMetadata.description,
        title=an_v3.structuralMetadata.title,
    )

    project: Project = Field(None, title="Project")

    datasetFilters: Optional[DatasetFilters] = Field(
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
    def save_schema(cls, location="./4.0.1/schema.json"):
        with open(location, "w") as f:
            json.dump(cls.model_json_schema(), f, indent=6)
