from hdr_schemata.models import remove_fields_from_cls
from hdr_schemata.models.HDRUK.v2_1_2 import Coverage as BaseCoverage
from hdr_schemata.definitions.HDRUK.BiologicalSamples import *
from typing import Optional, List
from pydantic import Field


from .annotations import annotations

an = annotations.coverage


class Coverage(BaseCoverage):
    class Config:
        extra = "forbid"

    gender: Optional[List[GenderType]] = Field(None, **an.gender.__dict__)

    biologicalsamples: Optional[List[BiologicalSampleType]] = Field(
        None,
        **an.gender.__dict__,
    )

    psychological: Optional[List[PsychologicalType]] = Field(
        None,
        **an.gender.__dict__,
    )

    physical: Optional[List[PhysicalType]] = Field(
        None,
        **an.gender.__dict__,
    )

    anthropometric: Optional[List[AnthropometricType]] = Field(
        None, **an.gender.__dict__
    )

    lifestyle: Optional[List[LifestylesType]] = Field(None, **an.gender.__dict__)

    socioeconomic: Optional[List[SocioEconomicType]] = Field(None, **an.gender.__dict__)


# inherited physicalSampleAvailability but this has now been replaced by biologicalsamples
remove_fields_from_cls(Coverage, ["physicalSampleAvailability"])
