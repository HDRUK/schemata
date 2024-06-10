from pydantic import BaseModel, Field
from typing import Optional, Union
from datetime import date, datetime
from hdr_schemata.definitions.HDRUK import *


from .annotations import annotations

an = annotations.provenance.temporal


class Temporal(BaseModel):
    class Config:
        extra = "forbid"

    publishingFrequency: PeriodicityV2 = Field(
        ..., **an.publishingFrequency.__dict__, json_schema_extra={"guidance": an.publishingFrequency.guidance}
    )

    distributionReleaseDate: Optional[Union[date, datetime]] = Field(
        None, **an.distributionReleaseDate.__dict__, json_schema_extra={"guidance": an.distributionReleaseDate.guidance}
    )

    startDate: Union[date, datetime] = Field(
        ..., **an.startDate.__dict__, json_schema_extra={"guidance": an.startDate.guidance}
    )
    
    endDate: Optional[Union[date, datetime, EndDateEnum]] = Field(
        None, **an.endDate.__dict__, json_schema_extra={"guidance": an.endDate.guidance}
    )

    timeLag: TimeLagV2 = Field(..., **an.timeLag.__dict__, json_schema_extra={"guidance": an.timeLag.guidance})
