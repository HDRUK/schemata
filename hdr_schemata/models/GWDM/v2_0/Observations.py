from datetime import datetime, date
from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *
from .annotations import annotations

an = annotations.observations


class Observation(BaseModel):
    class Config:
        extra = "forbid"

    measuredNode: StatisticalPopulationConstrainedV2 = Field(
        ..., **an.observedNode.__dict__
    )
    measuredValue: int = Field(..., **an.measuredValue.__dict__)
    disambiguatingDescription: Optional[AbstractText] = Field(
        None, **an.disambiguatingDescription.__dict__
    )
    observationDate: Union[date, datetime] = Field(..., **an.observationDate.__dict__)
    measuredProperty: MeasuredProperty = Field(..., **an.measuredProperty.__dict__)
