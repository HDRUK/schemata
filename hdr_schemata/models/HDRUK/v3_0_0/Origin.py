from typing import Optional, List, Union
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.provenance.origin


class Origin(BaseModel):
    class Config:
        extra = "forbid"

    purpose: Optional[List[PurposeV2]] = Field(None, **an.purpose.__dict__)

    datasetType: DatasetTypeV2 = Field(..., **an.datasetType.__dict__)

    datasetSubType: Optional[DatasetSubType] = Field(..., **an.datasetSubType.__dict__)
    
    source: Optional[List[SourceV2]] = Field(None, **an.source.__dict__)
    
    collectionSource: Optional[
        List[SettingV2]
    ] = Field(None, **an.collectionSource.__dict__)

    imageContrast: Optional[Ternary] = Field("Not stated", **an.imageContrast.__dict__)
