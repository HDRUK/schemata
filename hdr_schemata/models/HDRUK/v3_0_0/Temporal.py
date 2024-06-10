from pydantic import BaseModel, Field
from typing import Optional, Union
from datetime import date, datetime
from hdr_schemata.definitions.HDRUK import *


from .annotations import annotations

an = annotations.provenance.temporal


class Temporal(BaseModel):
    class Config:
        extra = "forbid"

    publishingFrequency: PeriodicityV2 = Field(..., **an.publishingFrequency.__dict__)

    distributionReleaseDate: Optional[Union[date, datetime]] = Field(
        None, **an.distributionReleaseDate.__dict__
    )

    startDate: Union[date, datetime] = Field(..., **an.startDate.__dict__)
    
    endDate: Optional[Union[date, datetime, EndDateEnum]] = Field(
        None, **an.endDate.__dict__
    )

    timeLag: TimeLagV2 = Field(..., **an.timeLag.__dict__)
