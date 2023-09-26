from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

class Usage(BaseModel):
    class Config:
        extra = 'forbid'

    dataUseLimitation: Optional[CommaSeparatedValues] = Field(
        ...,
        description='',
        title='Data Use Limitation',
    )
    dataUseRequirement: Optional[CommaSeparatedValues] = Field(
        ...,
        description='',
        title='Data Use Requirements',
    )
    resourceCreator: Optional[ShortDescription] = Field(
        None,
        description='',
        title='Citation Requirements',
    )
