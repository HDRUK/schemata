from typing import Optional, List
from pydantic import BaseModel, Field
from .TissueSampleMetadata import TissueSampleMetadata
from hdr_schemata.definitions.HDRUK import (
    TissueDataCategoriesEnum,
    TissueCollectionTypeEnum,
    MaterialTypeCategories,
)


class TissuesSampleCollection(BaseModel):
    dataCategories: Optional[List[TissueDataCategoriesEnum]] = Field(
        None,
        title="Data Categories",
        description="The type of data that is associated with the samples in the study. Can be several values MIABIS-2.0-13",
    )

    materialType: Optional[List[MaterialTypeCategories]] = Field(
        None,
        title="Material Type",
        description="The biospecimen saved from a biological entity for propagation e.g. testing, diagnostics, treatment or research purposes. Can be several values MIABIS-2.0-14",
    )

    tissueSampleMetadata: Optional[TissueSampleMetadata] = Field(
        None,
        title="Tissue Sample Metadata",
        description="Metadata related to the tissue sample",
    )

    collectionType: Optional[TissueCollectionTypeEnum] = Field(
        None,
        title="Collection Type",
        description="The type of the sample collection. Can be several values [MIABIS-2.0-16](https://github.com/BBMRI-ERIC/miabis/blob/master/Structured-data-and-lists.md#collection-type)",
    )
