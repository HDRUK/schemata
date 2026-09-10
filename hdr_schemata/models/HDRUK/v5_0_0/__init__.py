import json
from typing import Any, Dict, List, Optional

from pydantic import ConfigDict, Field

from hdr_schemata.models.HDRUK.v4_0_0 import Hdruk400

from .Accessibility import Accessibility
from .Coverage import Coverage
from .Distribution import Distribution
from .Provenance import Provenance
from .QualityAnnotation import QualityAnnotation
from .Summary import Summary


class Hdruk500(Hdruk400):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    context: Optional[str] = Field(
        "https://hdruk.github.io/schemata-2/context/5.0.0.jsonld",
        alias="@context",
        title="JSON-LD Context",
        description=(
            "URI of the JSON-LD context document that maps HDRUK field names to their "
            "DCAT, HealthDCAT-AP, and Dublin Core equivalents. When present, this document "
            "is directly consumable by a JSON-LD processor as a healthdcatap:HealthDataset."
        ),
    )
    id: Optional[str] = Field(
        None,
        alias="@id",
        title="Dataset URI",
        description="URI uniquely identifying this dataset record (dcat:Dataset identifier).",
    )
    type: Optional[str] = Field(
        "healthdcatap:HealthDataset",
        alias="@type",
        title="RDF Type",
        description=(
            "RDF type of this record. Defaults to healthdcatap:HealthDataset, "
            "which is a subclass of dcat:Dataset."
        ),
    )

    summary: Summary = Field(
        ...,
        title="Summary",
        description="High-level descriptive metadata about the dataset.",
    )

    coverage: Optional[Coverage] = Field(
        None,
        title="Coverage",
        description="Demographic and geographic coverage of the dataset population.",
    )

    accessibility: Accessibility = Field(
        ...,
        title="Accessibility",
        description="Access rights, permitted uses, and technical format information.",
    )

    provenance: Optional[Provenance] = Field(
        None,
        title="Provenance",
        description="Origin, temporal coverage, and retention information for the dataset.",
    )

    distributions: Optional[List[Distribution]] = Field(
        None,
        title="Distributions",
        description="DCAT-compliant distribution records for this dataset. Each distribution represents a specific downloadable or accessible form of the data (dcat:distribution).",
    )

    qualityAnnotations: Optional[List[QualityAnnotation]] = Field(
        None,
        title="Quality Annotations",
        description="Quality annotation records documenting data quality scores, certifications, or assessments (dqv:QualityAnnotation).",
    )

    @classmethod
    def model_json_schema(cls, by_alias: bool = True, **kwargs) -> Dict[str, Any]:
        return super().model_json_schema(by_alias=by_alias, **kwargs)

    @classmethod
    def save_schema(cls, location: str = "./5.0.0/schema.json") -> None:
        with open(location, "w") as f:
            json.dump(cls.model_json_schema(), f, indent=6)
