import json
from datetime import datetime
from typing import Any, Dict, List, Literal, Optional
from pydantic import BaseModel, ConfigDict, Field, constr, model_validator

from .Nodes import (
    Agent,
    ConceptRef,
    DocumentRef,
    Distribution,
    FrequencyRef,
    HealthAgent,
    Iri,
    Kind,
    LegalResourceRef,
    LinguisticSystemRef,
    LocationRef,
    NonNegativeInteger,
    PeriodOfTime,
    ProvenanceStatement,
    Purpose,
    RightsStatementRef,
    StandardRef,
    TableGroup,
)

from .annotations import annotations as an

NON_PUBLIC = "http://publications.europa.eu/resource/authority/access-right/NON_PUBLIC"
HEALTH_THEME = "http://publications.europa.eu/resource/authority/data-theme/HEAL"


class HealthDcatAp8(BaseModel):
    """
    A dcat:Dataset in HealthDCAT-AP Release 8, non-public profile, as compacted
    JSON-LD. Required fields follow the release's non-public SHACL shapes; the
    shapes stay the authority on conformance, this model only catches the
    structural mistakes early.
    """

    model_config = ConfigDict(extra="forbid", populate_by_name=True)

    context: Dict[str, Any] = Field(..., alias="@context", **an.context.__dict__)

    id: Iri = Field(..., alias="@id", **an.id.__dict__)

    type: Literal["Dataset"] = Field(..., alias="@type", **an.type.__dict__)

    identifier: List[constr(min_length=1)] = Field(..., min_length=1, **an.identifier.__dict__)

    title: constr(min_length=1) = Field(..., **an.title.__dict__)

    alternative: Optional[str] = Field(None, **an.alternative.__dict__)

    description: constr(min_length=1) = Field(..., **an.description.__dict__)

    version: Optional[str] = Field(None, **an.version.__dict__)

    issued: Optional[datetime] = Field(None, **an.issued.__dict__)

    modified: Optional[datetime] = Field(None, **an.modified.__dict__)

    landingPage: Optional[DocumentRef] = Field(None, **an.landingPage.__dict__)

    accessRights: RightsStatementRef = Field(..., **an.accessRights.__dict__)

    applicableLegislation: List[LegalResourceRef] = Field(
        ..., min_length=1, **an.applicableLegislation.__dict__
    )

    datasetType: List[ConceptRef] = Field(..., min_length=1, **an.datasetType.__dict__)

    theme: List[ConceptRef] = Field(..., min_length=1, **an.theme.__dict__)

    healthCategory: List[ConceptRef] = Field(..., min_length=1, **an.healthCategory.__dict__)

    healthTheme: Optional[List[ConceptRef]] = Field(None, **an.healthTheme.__dict__)

    keyword: List[constr(min_length=1)] = Field(..., min_length=1, **an.keyword.__dict__)

    contactPoint: List[Kind] = Field(..., min_length=1, **an.contactPoint.__dict__)

    publisher: HealthAgent = Field(..., **an.publisher.__dict__)

    creator: Optional[List[Agent]] = Field(None, **an.creator.__dict__)

    custodian: Optional[HealthAgent] = Field(None, **an.custodian.__dict__)

    hdab: HealthAgent = Field(..., **an.hdab.__dict__)

    temporal: Optional[List[PeriodOfTime]] = Field(None, **an.temporal.__dict__)

    accrualPeriodicity: Optional[FrequencyRef] = Field(None, **an.accrualPeriodicity.__dict__)

    spatial: Optional[List[LocationRef]] = Field(None, **an.spatial.__dict__)

    language: Optional[List[LinguisticSystemRef]] = Field(None, **an.language.__dict__)

    conformsTo: Optional[List[StandardRef]] = Field(None, **an.conformsTo.__dict__)

    hasCodingSystem: Optional[List[StandardRef]] = Field(None, **an.hasCodingSystem.__dict__)

    provenance: List[ProvenanceStatement] = Field(..., min_length=1, **an.provenance.__dict__)

    hasPurpose: Optional[List[Purpose]] = Field(None, **an.hasPurpose.__dict__)

    numberOfUniqueIndividuals: Optional[NonNegativeInteger] = Field(
        None, **an.numberOfUniqueIndividuals.__dict__
    )

    numberOfRecords: Optional[NonNegativeInteger] = Field(None, **an.numberOfRecords.__dict__)

    minTypicalAge: Optional[NonNegativeInteger] = Field(None, **an.minTypicalAge.__dict__)

    maxTypicalAge: Optional[NonNegativeInteger] = Field(None, **an.maxTypicalAge.__dict__)

    isReferencedBy: Optional[List[Iri]] = Field(None, **an.isReferencedBy.__dict__)

    isPartOf: Optional[List[Iri]] = Field(None, **an.isPartOf.__dict__)

    relation: Optional[List[Iri]] = Field(None, **an.relation.__dict__)

    hasStructuredData: bool = Field(..., **an.hasStructuredData.__dict__)

    hasVariables: Optional[List[TableGroup]] = Field(None, **an.hasVariables.__dict__)

    distribution: List[Distribution] = Field(..., min_length=1, **an.distribution.__dict__)

    @model_validator(mode="after")
    def non_public_profile(self):
        if self.accessRights.id != NON_PUBLIC:
            raise ValueError(f"accessRights must be {NON_PUBLIC} in the non-public profile")
        if HEALTH_THEME not in [t.id for t in self.theme]:
            raise ValueError(f"theme must include {HEALTH_THEME}")
        return self

    @model_validator(mode="after")
    def structured_data_has_variables(self):
        if self.hasStructuredData and not self.hasVariables:
            raise ValueError("hasVariables is required when hasStructuredData is true")
        if not self.hasStructuredData and self.hasVariables:
            raise ValueError("hasVariables must be empty when hasStructuredData is false")
        return self

    @model_validator(mode="after")
    def typical_age_range(self):
        if (
            self.minTypicalAge is not None
            and self.maxTypicalAge is not None
            and self.maxTypicalAge < self.minTypicalAge
        ):
            raise ValueError("maxTypicalAge cannot be below minTypicalAge")
        return self

    @classmethod
    def save_schema(cls, location="./8/schema.json"):
        with open(location, "w") as f:
            json.dump(cls.model_json_schema(), f, indent=6)
