from typing import Optional
from pydantic import BaseModel, Field
from .TissueSampleMetadata import TissueSampleMetadata
from hdr_schemata.definitions.HDRUK import CommaSeparatedValues


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
