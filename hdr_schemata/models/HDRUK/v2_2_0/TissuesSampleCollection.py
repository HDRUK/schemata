from typing import Optional, List
from pydantic import BaseModel, Field
from .TissueSampleMetadata import TissueSampleMetadata
from hdr_schemata.definitions.HDRUK import (
    TissueDataCategoriesEnum,
    TissueDataCategoriesEnum,
)


class TissuesSampleCollection(BaseModel):
    id: Optional[str] = Field(
        None, title="ID", description="ID of the tissue sample collection"
    )

    dataCategories: Optional[List[TissueDataCategoriesEnum]] = Field(
        None,
        title="Data Categories",
        description="Data categories related to the tissue sample collection",
    )

    materialType: Optional[CommaSeparatedValues] = Field(
        None,
        title="Material Type",
        description="Material type of the tissue sample collection",
    )

    tissueSampleMetadata: Optional[TissueSampleMetadata] = Field(
        None,
        title="Tissue Sample Metadata",
        description="Metadata related to the tissue sample",
    )
