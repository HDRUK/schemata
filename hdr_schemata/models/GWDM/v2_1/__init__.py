from __future__ import annotations

import json
from typing import Any, Dict, Optional

from pydantic import Field

from hdr_schemata.models.GWDM.v2_0 import Gwdm20
from hdr_schemata.models.HDRUK.v4_0_1 import Hdruk401
from hdr_schemata.models.HDRUK.v4_0_1.DatasetFilters import DatasetFilters
from hdr_schemata.models.HDRUK.v4_0_1.Icons import Icons
from hdr_schemata.models.HDRUK.v4_0_1.Image import Image
from hdr_schemata.models.HDRUK.v4_0_1.Project import Project

from .Summary import Summary


def _truncate(value: Optional[str], max_length: int) -> Optional[str]:
    if value is None:
        return None
    return value[:max_length]


class Gwdm21(Gwdm20):
    summary: Summary = Field(..., description="Summary of metadata describing key pieces of information.")
    icons: Optional[Icons] = Field(
        None,
        title="Icons",
        description="Calculated categorization icons added during export.",
    )
    project: Optional[Project] = Field(None, title="Project")
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
    def save_schema(cls, location: str = "./2.1/schema.json") -> None:
        with open(location, "w") as f:
            json.dump(cls.model_json_schema(), f, indent=6)

    def to_hdruk401_payload(self) -> Dict[str, Any]:
        summary = self.summary
        publisher = getattr(summary, "publisher", None)
        publisher_name = getattr(publisher, "name", None) if publisher else None
        publisher_id = None
        if publisher:
            publisher_id = getattr(publisher, "gatewayId", None) or getattr(publisher, "rorId", None)

        contact_point = getattr(summary, "contactPoint", None) or "unknown@example.com"

        keywords_value = getattr(summary, "keywords", None)
        if keywords_value is not None and hasattr(keywords_value, "root"):
            keywords_value = keywords_value.root
        keywords = None
        if isinstance(keywords_value, str):
            keywords = [k.strip() for k in keywords_value.split(",") if k.strip()] or None

        data_custodian = {
            "identifier": publisher_id or "unknown",
            "name": publisher_name or "Unknown",
            "contactPoint": contact_point,
        }

        funders_value = getattr(summary, "funders", None)
        if funders_value is not None and hasattr(funders_value, "root"):
            funders_value = funders_value.root

        payload: Dict[str, Any] = {
            "identifier": self.required.gatewayPid,
            "version": self.required.version,
            "revisions": self.required.revisions,
            "issued": self.required.issued,
            "modified": self.required.modified,
            "summary": {
                "title": _truncate(summary.title, 150),
                "funders": funders_value or publisher_name or "Unknown",
                "abstract": _truncate(summary.abstract, 500),
                "dataCustodian": data_custodian,
                "populationSize": summary.populationSize or 0,
                "keywords": keywords,
                "doiName": getattr(summary, "doiName", None),
                "contactPoint": contact_point,
            },
            "accessibility": self.accessibility,
            "observations": self.observations or [],
        }

        if self.coverage is not None:
            payload["coverage"] = self.coverage
        if self.provenance is not None:
            payload["provenance"] = self.provenance
        if self.demographicFrequency is not None:
            payload["demographicFrequency"] = self.demographicFrequency
        if self.omics is not None:
            payload["omics"] = self.omics
        if self.structuralMetadata is not None:
            payload["structuralMetadata"] = {"tables": self.structuralMetadata}
        if self.icons is not None:
            payload["icons"] = self.icons
        if self.project is not None:
            payload["project"] = self.project
        if self.datasetFilters is not None:
            payload["datasetFilters"] = self.datasetFilters
        if self.erd is not None:
            payload["erd"] = self.erd

        return payload

    def to_hdruk401(self) -> Hdruk401:
        return Hdruk401.model_validate(self.to_hdruk401_payload())
