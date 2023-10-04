from hdr_schemata.models.GWDM import Gwdm10
from hdr_schemata.models.GWDM.base import Coverage as BaseCoverage
from hdr_schemata.definitions.HDRUK import LongDescription

from typing import Optional
from pydantic import Field


class Coverage(BaseCoverage):
    lifestyle: Optional[LongDescription] = Field(
        None,
        title='Lifestyle',
        description='Description of cohort lifestyle habits: Smoking, Physical activity, Dietary habits, Alcohol'
    )


class Gwdm11(Gwdm10):
    #overload Coverage with an updated version of it.. 
    coverage: Optional[Coverage] = Field(
        None,
        description='Spatial and Temporal coverage',
        title='Coverage',
    )
