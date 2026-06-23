import json
from typing import Any, Dict, List, Optional

from pydantic import ConfigDict, Field

from hdr_schemata.definitions.HDRUK import Url
from hdr_schemata.models.HDRUK.v4_0_0 import Hdruk400

from .Accessibility import Accessibility
from .Coverage import Coverage
from .Distribution import Distribution
from .Provenance import Provenance
from .QualityAnnotation import QualityAnnotation
from .Summary import Summary
from .annotations import annotations as an


class Hdruk500(Hdruk400):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")

    # JSON-LD document identity — optional affordances for DCAT/HealthDCAT-AP interoperability
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

    # Extended sub-models
    summary: Summary = Field(
        ..., description=an.summary._description, title=an.summary._title
    )

    coverage: Optional[Coverage] = Field(
        None, description=an.coverage.description, title=an.coverage.title
    )

    accessibility: Accessibility = Field(
        ..., description=an.accessibility.description, title=an.accessibility.title
    )

    provenance: Optional[Provenance] = Field(
        None, description=an.provenance.description, title=an.provenance.title
    )

    # New top-level DCAT/DQV collections
    distributions: Optional[List[Distribution]] = Field(
        None,
        title=an.distributions.title,
        description=an.distributions.description,
    )

    qualityAnnotations: Optional[List[QualityAnnotation]] = Field(
        None,
        title=an.qualityAnnotations.title,
        description=an.qualityAnnotations.description,
    )

    @classmethod
    def model_json_schema(cls, by_alias: bool = True, **kwargs) -> Dict[str, Any]:
        """Override to default by_alias=True so @context/@id/@type appear in the schema."""
        return super().model_json_schema(by_alias=by_alias, **kwargs)

    @classmethod
    def save_schema(cls, location: str = "./5.0.0/schema.json") -> None:
        with open(location, "w") as f:
            json.dump(cls.model_json_schema(), f, indent=6)
