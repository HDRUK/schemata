from hdr_schemata.models import remove_fields_from_cls
from hdr_schemata.models.GWDM.v1_0 import Coverage as BaseCoverage
import re
from typing import Optional, List
from pydantic import Field
from hdr_schemata.definitions.HDRUK import CommaSeparatedValues

from .annotations import annotations

an = annotations.coverage


class Coverage(BaseCoverage):
    class Config:
        extra = "forbid"

    gender: Optional[CommaSeparatedValues] = Field(None, **an.gender.__dict__)

    biologicalsamples: Optional[CommaSeparatedValues] = Field(
        None, **an.biologicalsamples.__dict__
    )

    psychological: Optional[CommaSeparatedValues] = Field(
        None, **an.psychological.__dict__
    )

    physical: Optional[CommaSeparatedValues] = Field(None, **an.physical.__dict__)

    anthropometric: Optional[CommaSeparatedValues] = Field(
        None, **an.anthropometric.__dict__
    )

    lifestyle: Optional[CommaSeparatedValues] = Field(None, **an.lifestyle.__dict__)

    socioeconomic: Optional[CommaSeparatedValues] = Field(
        None, **an.socioeconomic.__dict__
    )


# inherited physicalSampleAvailability but this has now been replaced by biologicalsamples
remove_fields_from_cls(Coverage, ["physicalSampleAvailability"])
