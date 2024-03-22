from typing import Optional, List, Union
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *


from .annotations import annotations

an = annotations.coverage


class Coverage(BaseModel):
    class Config:
        extra = "forbid"

    spatial: Optional[Union[Optional[CommaSeparatedValues], List[Optional[Url]]]] = (
        Field(None, **an.spatial.__dict__)
    )

    typicalAgeRange: Optional[AgeRange] = Field(None, **an.typicalAgeRange.__dict__)

    physicalSampleAvailability: Optional[
        Union[Optional[CommaSeparatedValues], List]
    ] = Field(None, **an.physicalSampleAvailability.__dict__)

    followup: Optional[Followup] = Field("UNKNOWN", **an.followup.__dict__)

    pathway: Optional[Description] = Field(None, **an.pathway.__dict__)
