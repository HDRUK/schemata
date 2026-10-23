from typing import List, Literal, Optional
from pydantic import BaseModel, ConfigDict, EmailStr, Field, conint, constr, model_validator

# JSON-LD node objects used inside a HealthDCAT-AP 8 dataset. The "@id" and
# "@type" keys are aliased; the class names in "@type" resolve through
# context.jsonld.

Iri = constr(pattern=r"^(https?|mailto):\S+$")
NonNegativeInteger = conint(ge=0)


class Node(BaseModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)


# Typed references to an IRI from a controlled vocabulary or the web. They are
# typed in the document itself, as the HealthDCAT-AP examples do, so SHACL
# class checks pass without inference.


class ConceptRef(Node):
    id: Iri = Field(..., alias="@id")
    type: Literal["Concept"] = Field(..., alias="@type")


class LegalResourceRef(Node):
    id: Iri = Field(..., alias="@id")
    type: Literal["LegalResource"] = Field(..., alias="@type")


class RightsStatementRef(Node):
    id: Iri = Field(..., alias="@id")
    type: Literal["RightsStatement"] = Field(..., alias="@type")


class FrequencyRef(Node):
    id: Iri = Field(..., alias="@id")
    type: Literal["Frequency"] = Field(..., alias="@type")


class LinguisticSystemRef(Node):
    id: Iri = Field(..., alias="@id")
    type: Literal["LinguisticSystem"] = Field(..., alias="@type")


class LocationRef(Node):
    id: Iri = Field(..., alias="@id")
    type: Literal["Location"] = Field(..., alias="@type")


class StandardRef(Node):
    id: Iri = Field(..., alias="@id")
    type: Literal["Standard"] = Field(..., alias="@type")


class MediaTypeOrExtentRef(Node):
    id: Iri = Field(..., alias="@id")
    type: Literal["MediaTypeOrExtent"] = Field(..., alias="@type")


class DocumentRef(Node):
    id: Iri = Field(..., alias="@id")
    type: Literal["Document"] = Field(..., alias="@type")


class ContactPoint(Node):
    """cv:ContactPoint, used by agents. Needs an email or a contact page."""

    type: Literal["ContactPoint"] = Field(..., alias="@type")
    email: Optional[EmailStr] = None
    contactPage: Optional[Iri] = None

    @model_validator(mode="after")
    def email_or_page(self):
        if not self.email and not self.contactPage:
            raise ValueError("a ContactPoint needs email or contactPage")
        return self


class Kind(Node):
    """vcard:Kind, used by the dataset's dcat:contactPoint. Needs an email or a URL."""

    type: Literal["Kind"] = Field(..., alias="@type")
    hasEmail: Optional[constr(pattern=r"^mailto:\S+@\S+$")] = None
    hasURL: Optional[Iri] = None

    @model_validator(mode="after")
    def email_or_url(self):
        if not self.hasEmail and not self.hasURL:
            raise ValueError("a Kind needs hasEmail or hasURL")
        return self


class Agent(Node):
    """foaf:Agent for creator: name only."""

    id: Optional[Iri] = Field(None, alias="@id")
    type: Literal["Agent"] = Field(..., alias="@type")
    name: constr(min_length=1)


class HealthAgent(Agent):
    """foaf:Agent for publisher, custodian and hdab: exactly one cv:contactPoint."""

    contact: ContactPoint


class PeriodOfTime(Node):
    type: Literal["PeriodOfTime"] = Field(..., alias="@type")
    startDate: Optional[constr(pattern=r"^\d{4}-\d{2}-\d{2}$")] = None
    endDate: Optional[constr(pattern=r"^\d{4}-\d{2}-\d{2}$")] = None


class ProvenanceStatement(Node):
    type: Literal["ProvenanceStatement"] = Field(..., alias="@type")
    label: constr(min_length=1)


class Purpose(Node):
    type: Literal["Purpose"] = Field(..., alias="@type")
    description: constr(min_length=1)


class Column(Node):
    """csvw:Column. HealthDCAT-AP requires name, title, description and datatype."""

    type: Literal["Column"] = Field(..., alias="@type")
    columnName: constr(min_length=1)
    columnTitle: constr(min_length=1)
    description: constr(min_length=1)
    datatype: constr(min_length=1)


class Table(Node):
    type: Literal["Table"] = Field(..., alias="@type")
    title: constr(min_length=1)
    description: Optional[str] = None
    column: List[Column] = Field(..., min_length=1)


class TableGroup(Node):
    type: Literal["TableGroup"] = Field(..., alias="@type")
    title: constr(min_length=1)
    table: List[Table] = Field(..., min_length=1)


class Distribution(Node):
    type: Literal["Distribution"] = Field(..., alias="@type")
    title: constr(min_length=1)
    description: Optional[str] = None
    accessURL: Iri
    applicableLegislation: List[LegalResourceRef] = Field(..., min_length=1)
    format: Optional[MediaTypeOrExtentRef] = None
