from typing import List, Optional, Union
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK.BiologicalSamples import *
from hdr_schemata.definitions.HDRUK import *


from .annotations import annotations

an = annotations.coverage


class Coverage(BaseModel):
    class Config:
        extra = "forbid"
    
    spatial: Union[CommaSeparatedValues, List[Url]] = (
        Field(None, **an.spatial.__dict__)
    )

    typicalAgeRangeMin: Optional[int] = Field(None, **an.typicalAgeRangeMin.__dict__)

    typicalAgeRangeMax: Optional[int] = Field(None, **an.typicalAgeRangeMax.__dict__)

    datasetCompleteness: Optional[Url] = (
        Field(None, **an.datasetCompleteness.__dict__)
    )

    materialType: List[MaterialTypeCategoriesV2] = Field(
        "None/not available", **an.materialType.__dict__
    )

    followup: Optional[Followup] = Field("UNKNOWN", **an.followup.__dict__)

    pathway: Optional[Description] = Field(None, **an.pathway.__dict__)

    gender: Optional[List[GenderType]] = Field(None, **an.gender.__dict__)
