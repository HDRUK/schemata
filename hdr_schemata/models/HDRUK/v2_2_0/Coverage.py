from hdr_schemata.models import remove_fields_from_cls
from hdr_schemata.models.HDRUK.v2_1_2 import Coverage as BaseCoverage
from hdr_schemata.definitions.HDRUK.BiologicalSamples import *
from typing import Optional, List
from pydantic import Field


class Coverage(BaseCoverage):
    class Config:
        extra = "forbid"

    gender: Optional[List[GenderType]] = Field(
        None, title="Gender", description="Male, Female, Other"
    )

    biologicalsamples: Optional[List[BiologicalSampleType]] = Field(
        None, title="Biological Samples", description="Blood, Saliva, Urine, Other"
    )

    psychological: Optional[List[PsychologicalType]] = Field(
        None, title="Psychological", description="Mental health, Cognitive function"
    )

    physical: Optional[List[PhysicalType]] = Field(
        None,
        title="Physical",
        description="Cardiovascular, Respiratory, Musculoskeletal, Hearing and Vision, Reproductive",
    )

    anthropometric: Optional[List[AnthropometricType]] = Field(
        None,
        title="Anthropometric",
        description="Height, Weight, Waist circumference, Hip circumference, Blood pressure",
    )

    lifestyle: Optional[List[LifestylesType]] = Field(
        None,
        title="Lifestyle",
        description="Cohort lifestyle habits: Smoking, Physical activity, Dietary habits, Alcohol",
    )

    socioeconomic: Optional[List[SocioEconomicType]] = Field(
        None,
        title="Socio-economic",
        description="Occupation, Family circumstances, Housing, Education, Ethnic group, Martial status, Social support",
    )


# inherited physicalSampleAvailability but this has now been replaced by biologicalsamples
remove_fields_from_cls(Coverage, ["physicalSampleAvailability"])
