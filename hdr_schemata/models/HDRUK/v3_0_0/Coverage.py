from typing import List, Optional, Union
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK.BiologicalSamples import *
from hdr_schemata.definitions.HDRUK import *


from .annotations import annotations

an = annotations.coverage


class Coverage(BaseModel):
    class Config:
        extra = "forbid"

    spatial: Union[CommaSeparatedValues, List[Url]] = Field(
        None, **an.spatial.__dict__, json_schema_extra={"guidance": an.spatial.guidance}
    )

    typicalAgeRangeMin: Optional[int] = Field(
        None,
        **an.typicalAgeRangeMin.__dict__,
        json_schema_extra={"guidance": an.typicalAgeRangeMin.guidance}
    )

    typicalAgeRangeMax: Optional[int] = Field(
        None,
        **an.typicalAgeRangeMax.__dict__,
        json_schema_extra={"guidance": an.typicalAgeRangeMax.guidance}
    )

    datasetCompleteness: Optional[Url] = Field(
        None,
        **an.datasetCompleteness.__dict__,
        json_schema_extra={"guidance": an.datasetCompleteness.guidance}
    )

    materialType: Optional[List[MaterialTypeCategoriesV2]] = Field(
        None,
        **an.materialType.__dict__,
        json_schema_extra={"guidance": an.materialType.guidance}
    )

    followUp: Optional[FollowupV2] = Field(
        "UNKNOWN",
        **an.followUp.__dict__,
        json_schema_extra={"guidance": an.followUp.guidance}
    )

    pathway: Optional[Description] = Field(
        None, **an.pathway.__dict__, json_schema_extra={"guidance": an.pathway.guidance}
    )

    gender: Optional[List[GenderType]] = Field(
        None, **an.gender.__dict__, json_schema_extra={"guidance": an.gender.guidance}
    )
