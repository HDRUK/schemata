from datetime import date, datetime
from typing import Optional, List, Union
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from hdr_schemata.annotations import annotations

an = annotations.HDRUK.v2p1p2.provenance.temporal


class Temporal(BaseModel):
    class Config:
        extra = "forbid"

    accrualPeriodicity: Periodicity = Field(..., **an.accrualPeriodicity.__dict__)
    distributionReleaseDate: Optional[Union[date, datetime]] = Field(
        None, **an.accrualPeriodicity.__dict__
    )
    startDate: Optional[Union[date, datetime]] = Field(..., **an.startDate.__dict__)
    endDate: Optional[Union[date, datetime, EndDateEnum]] = Field(
        None, **an.endDate.__dict__
    )
    timeLag: TimeLag = Field(..., **an.timeLag.__dict__)
