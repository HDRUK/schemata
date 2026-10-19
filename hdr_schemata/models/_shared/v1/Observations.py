from hdr_schemata.definitions.HDRUK import *
from typing import Optional, Union
from pydantic import BaseModel, Field
from datetime import date, datetime

from .annotations import annotations

an = annotations.observations

class Observation(BaseModel):
    class Config:
        extra = "forbid" 
    
    observedNode: StatisticalPopulationConstrainedV2 = Field(
        ..., **an.observedNode.__dict__, json_schema_extra={"guidance": an.observedNode.guidance}
    )

    measuredValue: int = Field(..., **an.measuredValue.__dict__, json_schema_extra={"guidance": an.measuredValue.guidance})

    disambiguatingDescription: Optional[AbstractText] = Field(
        None, **an.disambiguatingDescription.__dict__, json_schema_extra={"guidance": an.disambiguatingDescription.guidance}
    )

    observationDate: Union[date, datetime] = Field(
        ..., 
        **an.observationDate.__dict__, 
        json_schema_extra={"guidance": an.observationDate.guidance}
    )

    measuredProperty: MeasuredProperty = Field(
        ..., **an.measuredProperty.__dict__, json_schema_extra={"guidance": an.measuredProperty.guidance}
    )
