from typing import Optional
from pydantic import BaseModel, Field

from hdr_schemata.definitions.HDRUK.CommaSeparatedValues import CommaSeparatedValuesV2
from .TissueSampleMetadata import TissueSampleMetadata



from .annotations import annotations

an = annotations.tissuesSampleCollection


class TissuesSampleCollection(BaseModel):
    id: Optional[CommaSeparatedValuesV2] = Field(None, **an.id.__dict__)

    dataCategories: Optional[CommaSeparatedValuesV2] = Field(
        None, **an.dataCategories.__dict__
    )

    materialType: Optional[CommaSeparatedValuesV2] = Field(
        None, **an.materialType.__dict__
    )

    accessConditions: Optional[CommaSeparatedValuesV2] = Field(
        None, **an.accessConditions.__dict__
    )

    collectionType: Optional[CommaSeparatedValuesV2] = Field(
        None, **an.collectionType.__dict__
    )

    disease: Optional[CommaSeparatedValuesV2] = Field(None, **an.disease.__dict__)

    storageTemperature: Optional[CommaSeparatedValuesV2] = Field(
        None, **an.storageTemperature.__dict__
    )

    sampleAgeRange: Optional[CommaSeparatedValuesV2] = Field(
        None, **an.sampleAgeRange.__dict__
    )

    tissueSampleMetadata: Optional[TissueSampleMetadata] = Field(
        None,
        title=an.tissueSampleMetadata.title,
        description=an.tissueSampleMetadata.description,
    )
