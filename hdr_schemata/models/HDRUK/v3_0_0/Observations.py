from hdr_schemata.models.HDRUK.v2_2_1 import Observation as BaseObservation
from hdr_schemata.definitions.HDRUK import *
from typing import Optional, Union
from pydantic import Field
from datetime import date, datetime

from .annotations import annotations

an = annotations.observations

class Observation(BaseObservation):
    
    observedNode: StatisticalPopulationConstrainedV2 = Field(
        ..., **an.observedNode.__dict__
    )

    measuredValue: int = Field(..., **an.measuredValue.__dict__)

    disambiguatingDescription: Optional[AbstractText] = Field(
        None, **an.disambiguatingDescription.__dict__
    )

    observationDate: Union[date, datetime] = Field(..., **an.observationDate.__dict__)

    measuredProperty: MeasuredProperty = Field(..., **an.measuredProperty.__dict__)


