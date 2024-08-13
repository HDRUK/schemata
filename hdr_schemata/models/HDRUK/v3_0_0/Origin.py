from typing import Optional, List, Union
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.provenance.origin


class Origin(BaseModel):
    class Config:
        extra = "forbid"

    purpose: Optional[List[PurposeV2]] = Field(
        None, **an.purpose.__dict__, json_schema_extra={"guidance": an.purpose.guidance}
    )

    datasetType: List[DatasetTypeV2] = Field(
        ..., **an.datasetType.__dict__, json_schema_extra={"guidance": an.datasetType.guidance}
    )

    datasetSubType: Optional[List[DatasetSubType]] = Field(
        ..., **an.datasetSubType.__dict__, json_schema_extra={"guidance": an.datasetSubType.guidance}
    )
    
    source: Optional[List[SourceV2]] = Field(
        None, **an.source.__dict__, json_schema_extra={"guidance": an.source.guidance}
    )
    
    collectionSource: Optional[
        List[SettingV2]
    ] = Field(
        None, **an.collectionSource.__dict__, json_schema_extra={"guidance": an.collectionSource.guidance}
    )

    imageContrast: Optional[Ternary] = Field(
        "Not stated", **an.imageContrast.__dict__, json_schema_extra={"guidance": an.imageContrast.guidance}
    )
