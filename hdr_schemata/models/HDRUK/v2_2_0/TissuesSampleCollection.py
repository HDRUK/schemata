from typing import Optional, List
from pydantic import BaseModel, Field
from .TissueSampleMetadata import TissueSampleMetadata
from hdr_schemata.definitions.HDRUK import (
    TissueDataCategoriesEnum,
    TissueCollectionTypeEnum,
    MaterialTypeCategories,
)

from .annotations import annotations

an = annotations.tissuesSampleCollection


class TissuesSampleCollection(BaseModel):
    dataCategories: Optional[List[TissueDataCategoriesEnum]] = Field(
        None, **an.dataCategories.__dict__
    )

    materialType: Optional[List[MaterialTypeCategories]] = Field(
        None, **an.materialType.__dict__
    )

    tissueSampleMetadata: Optional[TissueSampleMetadata] = Field(
        None,
        title=an.tissueSampleMetadata.title,
        description=an.tissueSampleMetadata.description,
    )

    collectionType: Optional[TissueCollectionTypeEnum] = Field(
        None, **an.collectionType.__dict__
    )
