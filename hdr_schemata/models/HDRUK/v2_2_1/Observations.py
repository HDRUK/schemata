from hdr_schemata.models.HDRUK.v2_2_0 import Observation as BaseObservation
from pydantic import Field
from .MeasuredProperty import MeasuredProperty

from .annotations import annotations

an = annotations.observations

class Observation(BaseObservation):
    measuredProperty: MeasuredProperty = Field(..., **an.measuredProperty.__dict__)
