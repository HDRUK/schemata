from typing import Optional, List, Union
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.demographicFrequency


class DemographicFrequency(BaseModel):
    class Config:
        extra = "forbid"

    age: Optional[List[Age]] = Field(
        ..., 
        **an.age.__dict__, 
        # json_schema_extra={"guidance": an.age.guidance}
    )

    ethnicity: Optional[List[Ethnicity]] = Field(
        ..., **an.ethnicity.__dict__, # json_schema_extra={"guidance": an.ethnicity.guidance}
    )

    genderAssignedAtBirth: Optional[List[GenderAssignedAtBirth]] = Field(
        ..., **an.genderAssignedAtBirth.__dict__, # json_schema_extra={"guidance": an.genderAssignedAtBirth.guidance}
    )

    disease: Optional[List[Disease]] = Field(
        ..., **an.disease.__dict__, # json_schema_extra={"guidance": an.disease.guidance}
    )
