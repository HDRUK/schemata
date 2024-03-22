from typing import Optional
from pydantic import BaseModel, Field
from .TissueSampleMetadata import TissueSampleMetadata
from hdr_schemata.definitions.HDRUK import CommaSeparatedValues


from .annotations import annotations

an = annotations.tissuesSampleCollection


class TissuesSampleCollection(BaseModel):
    id: Optional[CommaSeparatedValues] = Field(None, **an.id.__dict__)

    dataCategories: Optional[CommaSeparatedValues] = Field(
        None, **an.dataCategories.__dict__
    )

    materialType: Optional[CommaSeparatedValues] = Field(
        None, **an.materialType.__dict__
    )

    accessConditions: Optional[CommaSeparatedValues] = Field(
        None, **an.accessConditions.__dict__
    )

    collectionType: Optional[CommaSeparatedValues] = Field(
        None, **an.collectionType.__dict__
    )

    disease: Optional[CommaSeparatedValues] = Field(None, **an.disease.__dict__)

    storageTemperature: Optional[CommaSeparatedValues] = Field(
        None, **an.storageTemperature.__dict__
    )

    sampleAgeRange: Optional[CommaSeparatedValues] = Field(
        None, **an.sampleAgeRange.__dict__
    )

    tissueSampleMetadata: Optional[TissueSampleMetadata] = Field(
        None,
        title=an.tissueSampleMetadata.title,
        description=an.tissueSampleMetadata.description,
    )
