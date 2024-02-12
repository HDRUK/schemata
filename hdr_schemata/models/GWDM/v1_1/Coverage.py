from hdr_schemata.models import remove_fields_from_cls
from hdr_schemata.models.GWDM.v1_0 import Coverage as BaseCoverage
import re
from typing import Optional, List
from pydantic import Field
from hdr_schemata.definitions.HDRUK import CommaSeparatedValues


class Coverage(BaseCoverage):
    class Config:
        extra = "forbid"

    gender: Optional[CommaSeparatedValues] = Field(
        None, title="Gender", description="Male, Female, Other"
    )

    biologicalsamples: Optional[CommaSeparatedValues] = Field(
        None, title="Biological Samples", description="Blood, Saliva, Urine, Other"
    )

    psychological: Optional[CommaSeparatedValues] = Field(
        None, title="Psychological", description="Mental health, Cognitive function"
    )

    physical: Optional[CommaSeparatedValues] = Field(
        None,
        title="Physical",
        description="Cardiovascular, Respiratory, Musculoskeletal, Hearing and Vision, Reproductive",
    )

    anthropometric: Optional[CommaSeparatedValues] = Field(
        None,
        title="Anthropometric",
        description="Height, Weight, Waist circumference, Hip circumference, Blood pressure",
    )

    lifestyle: Optional[CommaSeparatedValues] = Field(
        None,
        title="Lifestyle",
        description="Cohort lifestyle habits: Smoking, Physical activity, Dietary habits, Alcohol",
    )

    socioeconomic: Optional[CommaSeparatedValues] = Field(
        None,
        title="Socio-economic",
        description="Occupation, Family circumstances, Housing, Education, Ethnic group, Marital status, Social support",
    )


# inherited physicalSampleAvailability but this has now been replaced by biologicalsamples
remove_fields_from_cls(Coverage, ["physicalSampleAvailability"])
