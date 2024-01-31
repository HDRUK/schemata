from typing import Optional, List
from pydantic import BaseModel, Field
from .TissueSampleMetadata import TissueSampleMetadata
from hdr_schemata.definitions.HDRUK import (
    TissueDataCategoriesEnum,
    MaterialTypeCategories,
)


class TissuesSampleCollection(BaseModel):
    dataCategories: Optional[List[TissueDataCategoriesEnum]] = Field(
        None,
        title="Data Categories",
        description="Data categories related to the tissue sample collection",
    )

    materialType: Optional[List[MaterialTypeCategories]] = Field(
        None,
        title="Material Type",
        description="Material type of the tissue sample collection",
    )

    tissueSampleMetadata: Optional[TissueSampleMetadata] = Field(
        None,
        title="Tissue Sample Metadata",
        description="Metadata related to the tissue sample",
    )
