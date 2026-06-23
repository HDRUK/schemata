from typing import Optional

from pydantic import Field

from hdr_schemata.models.HDRUK.v3_0_0.Access import Access as Access300


class Access(Access300):

    legalBasis: Optional[str] = Field(
        None,
        title="Legal Basis",
        description="Legal basis under which personal data in this dataset is processed (dpv:hasLegalBasis). Reference the relevant legislation or DPV concept, e.g. 'GDPR Art.9(2)(j) - scientific research'.",
    )

    applicableLegislation: Optional[str] = Field(
        None,
        title="Applicable Legislation",
        description="Legislation governing the access and use of this dataset (dcatap:applicableLegislation), e.g. 'UK GDPR', 'Health and Social Care (Safety and Quality) Act 2015'.",
    )

    personalData: Optional[str] = Field(
        None,
        title="Personal Data",
        description="Description of the categories of personal data held in the dataset (dpv:hasPersonalData). Reference DPV personal data categories or describe the types of identifiers and sensitive data present.",
    )
