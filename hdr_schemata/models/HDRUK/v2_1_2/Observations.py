from datetime import datetime, date
from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

from hdr_schemata.annotations import annotations

an = annotations.HDRUK.v2p1p2.observations


class Observation(BaseModel):
    class Config:
        extra = "forbid"

    observedNode: StatisticalPopulationConstrained = Field(
        ..., **an.observedNode.__dict__
    )
    measuredValue: int = Field(..., **an.measuredValue.__dict__)
    disambiguatingDescription: Optional[AbstractText] = Field(
        None, **an.disambiguatingDescription.__dict__
    )
    observationDate: Union[date, datetime] = Field(..., **an.observationDate.__dict__)
    measuredProperty: MeasuredProperty = Field(..., **an.measuredProperty.__dict__)
