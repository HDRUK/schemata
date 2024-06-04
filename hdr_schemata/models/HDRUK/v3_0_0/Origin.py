from hdr_schemata.models.HDRUK.v2_2_1.Origin import Origin as BaseOrigin
from hdr_schemata.models import remove_fields_from_cls
from typing import Optional, List, Union
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.provenance.origin


class Origin(BaseOrigin):

    purpose: Optional[List[PurposeV2]] = Field(None, **an.purpose.__dict__)
    
    source: Optional[List[SourceV2]] = Field(None, **an.source.__dict__)
    
    collectionSource: Optional[
        List[SettingV2]
    ] = Field(None, **an.collectionSource.__dict__)

    datasetType: DatasetTypeV2 = Field(..., **an.datasetType.__dict__)

    datasetSubType: Optional[DatasetSubType] = Field(..., **an.datasetSubType.__dict__)

    imageContrast: Optional[Ternary] = Field("Not stated", **an.imageContrast.__dict__)

remove_fields_from_cls(Origin, ["collectionSituation"])