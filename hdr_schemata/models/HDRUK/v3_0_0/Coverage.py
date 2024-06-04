from hdr_schemata.models.HDRUK.v2_2_0 import Coverage as BaseCoverage
from hdr_schemata.models import remove_fields_from_cls
from typing import List, Optional, Union
from pydantic import Field
from hdr_schemata.definitions.HDRUK import *


from .annotations import annotations

an = annotations.coverage


class Coverage(BaseCoverage):
    
    spatial: Union[CommaSeparatedValues, List[Url]] = (
        Field(None, **an.spatial.__dict__)
    )

    typicalAgeRange: Optional[AgeRange] = Field(None, **an.typicalAgeRange.__dict__)

    followup: Optional[Followup] = Field("UNKNOWN", **an.followup.__dict__)

    pathway: Optional[Description] = Field(None, **an.pathway.__dict__)
    
    datasetCompleteness: Optional[Url] = (
        Field(None, **an.datasetCompleteness.__dict__)
    )
    

remove_fields_from_cls(Coverage, [
    "physicalSampleAvailability",
    "biologicalsamples",
    "psychological",
    "physical",
    "anthropometric",
    "lifestyle",
    "socioeconomic"
])
