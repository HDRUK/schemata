from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

from hdr_schemata.definitions.HDRUK import *

from .Required import Required
from .Summary import Summary


class GwdmBaseModel(BaseModel):
    class Config:
        extra = 'forbid'


    required: Required

    summary: Summary = Field(
        ...,
        description='Summary metadata must be completed by Data Custodians onboarding metadata into the Innovation Gateway MVP.',
        title='Summary',
    )
    

