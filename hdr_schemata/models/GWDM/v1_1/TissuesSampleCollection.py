from typing import Optional
from pydantic import BaseModel, Field
from .TissueSampleMetadata import TissueSampleMetadata
from hdr_schemata.definitions.HDRUK import CommaSeparatedValues


class TissueSampleDonor(BaseModel):
    id: Optional[CommaSeparatedValues] = Field(
        None, title="Donor ID", description="ID of the sample donor"
    )
    sex: Optional[CommaSeparatedValues] = Field(
        None, title="Donor Sex", description="Sex of the sample donor"
    )
    dataCategories: Optional[CommaSeparatedValues] = Field(
        None,
        title="Donor Data Categories",
        description="Data categories related to the sample donor",
    )


class TissueSampleMetadata(BaseModel):
    id: Optional[CommaSeparatedValues] = Field(
        None, title="Metadata ID", description="ID of the tissue sample metadata"
    )
    sampleDonor: TissueSampleDonor = Field(
        None, title="Sample Donor", description="Information about the sample donor"
    )
    sampleType: Optional[CommaSeparatedValues] = Field(
        None, title="Sample Type", description="Type of the tissue sample"
    )
    storageTemperature: Optional[CommaSeparatedValues] = Field(
        None,
        title="Storage Temperature",
        description="Storage temperature of the tissue sample",
    )
    creationDate: Optional[CommaSeparatedValues] = Field(
        None,
        title="Creation Date",
        description="Date when the tissue sample metadata was created",
    )
    AnatomicalSiteOntologyCode: Optional[CommaSeparatedValues] = Field(
        None,
        title="Anatomical Site Ontology Code",
        description="Ontology code for the anatomical site",
    )
    AnatomicalSiteOntologyDescription: Optional[CommaSeparatedValues] = Field(
        None,
        title="Anatomical Site Ontology Description",
        description="Ontology description for the anatomical site",
    )
    AnatomicalSiteFreeText: Optional[CommaSeparatedValues] = Field(
        None,
        title="Anatomical Site Free Text",
        description="Free text describing the anatomical site",
    )
    sampleContentDiagnosis: Optional[CommaSeparatedValues] = Field(
        None,
        title="Sample Content Diagnosis",
        description="Diagnosis related to the sample content",
    )
    useReCommaSeparatedValuesictions: Optional[CommaSeparatedValues] = Field(
        None,
        title="Use Restrictions",
        description="Restrictions on the use of the tissue sample",
    )


class TissuesSampleCollection(BaseModel):
    id: Optional[CommaSeparatedValues] = Field(
        None, title="ID", description="ID of the tissue sample collection"
    )

    dataCategories: Optional[CommaSeparatedValues] = Field(
        None,
        title="Data Categories",
        description="Data categories related to the tissue sample collection",
    )

    materialType: Optional[CommaSeparatedValues] = Field(
        None,
        title="Material Type",
        description="Material type of the tissue sample collection",
    )

    accessConditions: Optional[CommaSeparatedValues] = Field(
        None,
        title="Access Conditions",
        description="Access conditions for the tissue sample collection",
    )

    collectionType: Optional[CommaSeparatedValues] = Field(
        None,
        title="Collection Type",
        description="Type of the tissue sample collection",
    )

    disease: Optional[CommaSeparatedValues] = Field(
        None,
        title="Disease",
        description="Disease associated with the tissue sample collection",
    )

    storageTemperature: Optional[CommaSeparatedValues] = Field(
        None,
        title="Storage Temperature",
        description="Storage temperature of the tissue sample collection",
    )

    sampleAgeRange: Optional[CommaSeparatedValues] = Field(
        None,
        title="Sample Age Range",
        description="Age range of the tissue sample collection",
    )

    tissueSampleMetadata: Optional[TissueSampleMetadata] = Field(
        None,
        title="Tissue Sample Metadata",
        description="Metadata related to the tissue sample",
    )
