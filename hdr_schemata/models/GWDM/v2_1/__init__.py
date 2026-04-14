from __future__ import annotations

import json
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, constr

from hdr_schemata.models.GWDM.v2_0 import Gwdm20
from hdr_schemata.models.CRUK.v1_0_0 import Cruk100, DatasetFilter as CrukDatasetFilter
from hdr_schemata.models.HDRUK.v4_0_0 import Hdruk400
from hdr_schemata.definitions.HDRUK import Description, OneHundredFiftyCharacters

from .Summary import LineSeparatedValues, Summary


DatasetFilterItem = constr(
    pattern=r'\{\s*"id":\s*"(\d+_){0,5}\d+",\s*"label":\s*".{0,150}",\s*"category":\s*".{0,150}",\s*"primaryGroup":\s*"(cancer-type|data-type|access-type)",\s*"description":\s*".{0,150}"\s*\}'
)


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


class Project(BaseModel):
    class Config:
        extra = "forbid"

    projectName: Optional[OneHundredFiftyCharacters] = Field(
        None,
        title="Project Title",
        description="May or may not be different to the Dataset Title",
    )
    leadResearcher: Optional[OneHundredFiftyCharacters] = Field(
        None,
        title="Lead Researcher",
        examples=["Dr Smith"],
        description="",
    )
    leadResearchInstitute: Optional[OneHundredFiftyCharacters] = Field(
        None,
        title="Lead Research Institute",
        examples=["Sussex University"],
        description="",
    )
    grantNumbers: Optional[LineSeparatedValues] = Field(
        None,
        title="Grant number(s)",
        description="List of grant numbers separated by a line break",
        examples=["A354t", "ropguadg"],
        json_schema_extra={"guidance": "Normally specified on the grant acceptance letter"},
    )
    projectStartDate: Optional[str] = Field(
        None,
        title="Project Start Date",
        description="Starting date of project grant.",
        json_schema_extra={
            "guidance": (
                "Date on which the dataset project starts. This is normally set out in the grant contract "
                "and will be different from the start of any data collection"
            )
        },
    )
    projectEndDate: Optional[str] = Field(
        None,
        title="Project End Date",
        description="Current end date of project grant.",
        json_schema_extra={
            "guidance": (
                "Date on which the dataset project is currently projected to finish. This is normally set "
                "out in the grant contract and will be different from the end of any data collection"
            )
        },
    )
    projectScope: Optional[constr(min_length=5, max_length=500)] = Field(
        None,
        title="Project Scope",
        description="data and biospecimens expected to result from the grant.",
        examples=["Longitudinal genomic data including somatic mutations"],
        json_schema_extra={
            "guidance": (
                "Short paragraph setting out the types of data / biospecimens likely to result from the "
                "grant and the cancers covered"
            )
        },
    )


def _truncate(value: Optional[str], max_length: int) -> Optional[str]:
    if value is None:
        return None
    if hasattr(value, "root"):
        value = value.root
    return value[:max_length]


class Gwdm21(Gwdm20):
    summary: Summary = Field(..., description="Summary of metadata describing key pieces of information.")
    icons: Optional[List[str]] = Field(
        None,
        title="Icons",
        description="Calculated categorization icons added during export.",
    )
    project: Optional[Project] = Field(None, title="Project")
    datasetFilters: Optional[List[DatasetFilterItem]] = Field(
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

    def to_hdruk400_payload(self) -> Dict[str, Any]:
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

        revisions_value = self.required.revisions
        if revisions_value is not None and hasattr(revisions_value, "root"):
            revisions_value = revisions_value.root
        if isinstance(revisions_value, list):
            revisions_value = [
                r.model_dump(mode="json") if hasattr(r, "model_dump") else r for r in revisions_value
            ]

        observations_value = self.observations or []
        if isinstance(observations_value, list):
            observations_value = [
                o.model_dump(mode="json") if hasattr(o, "model_dump") else o for o in observations_value
            ]

        accessibility_value = (
            self.accessibility.model_dump(mode="json")
            if hasattr(self.accessibility, "model_dump")
            else self.accessibility
        )

        payload: Dict[str, Any] = {
            # HDRUK allows uuid/url identifiers; gatewayId is the closest.
            "identifier": self.required.gatewayId,
            "version": self.required.version,
            "revisions": revisions_value or [],
            "issued": self.required.issued,
            "modified": self.required.modified,
            "summary": {
                "title": _truncate(summary.title, 150),
                "abstract": _truncate(summary.abstract, 500),
                "dataCustodian": data_custodian,
                "populationSize": summary.populationSize or 0,
                "keywords": keywords,
                "doiName": getattr(summary, "doiName", None),
                "contactPoint": contact_point,
            },
            "accessibility": accessibility_value,
            "observations": observations_value,
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
        return payload

    def to_hdruk400(self) -> Hdruk400:
        return Hdruk400.model_validate(self.to_hdruk400_payload())

    def to_cruk100_payload(self) -> Dict[str, Any]:
        payload = self.to_hdruk400_payload()

        # CRUK 1.0.0 extends HDRUK 4.0.0 with additional fields.
        # GWDM 2.1 already has these fields, so pass them through.
        if self.icons is not None:
            payload["icons"] = self.icons
        if self.datasetFilters is not None:
            filters: List[Dict[str, Any]] = []
            for item in self.datasetFilters:
                if item is None:
                    continue
                raw = item.root if hasattr(item, "root") else item
                if not isinstance(raw, str):
                    continue
                try:
                    obj = json.loads(raw)
                except Exception:
                    continue
                if isinstance(obj, dict):
                    # Validate/normalize against CRUK DatasetFilter shape
                    filters.append(CrukDatasetFilter.model_validate(obj).model_dump(mode="json"))
            payload["datasetFilters"] = filters or None
        if self.erd is not None:
            # CRUK expects a URL; GWDM carries an Image object. Prefer the image string if present.
            image_value = getattr(self.erd, "image", None)
            if image_value is not None and hasattr(image_value, "root"):
                image_value = image_value.root
            payload["erd"] = image_value

        return payload

    def to_cruk100(self) -> Cruk100:
        return Cruk100.model_validate(self.to_cruk100_payload())
