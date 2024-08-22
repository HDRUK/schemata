from typing import Optional, List, Union
from pydantic import BaseModel, Field

from .annotations import annotations

from .Age import Age
from .Disease import Disease
from .Ethnicity import Ethnicity

an = annotations.demographicFrequency


class DemographicFrequency(BaseModel):
    class Config:
        extra = "forbid"

    age: Optional[List[Age]] = Field(
        None, 
        title=an.age.title,
        description=an.age.description,
        # json_schema_extra={"guidance": an.age.guidance}
    )

    ethnicity: Optional[List[Ethnicity]] = Field(
        None,
        title=an.ethnicity.title,
        description=an.ethnicity.description,
        # json_schema_extra={"guidance": an.ethnicity.guidance}
    )

    disease: Optional[List[Disease]] = Field(
        None,
        title=an.disease.title,
        description=an.disease.description,
        # json_schema_extra={"guidance": an.disease.guidance}
    )
