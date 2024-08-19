from datetime import date, datetime
from typing import Optional, List, Union
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.provenance.temporal


class Temporal(BaseModel):
    class Config:
        extra = "forbid"

    startDate: Optional[Union[date, datetime]] = Field(None, **an.startDate.__dict__)
    endDate: Optional[Union[date, datetime]] = Field(None, **an.endDate.__dict__)
    timeLag: TimeLagV2 = Field(..., **an.timeLag.__dict__)

    accrualPeriodicity: PeriodicityV2 = Field(..., **an.accrualPeriodicity.__dict__)

    distributionReleaseDate: Optional[Union[date, datetime]] = Field(
        None, **an.distributionReleaseDate.__dict__
    )
