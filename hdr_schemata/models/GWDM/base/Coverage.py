from datetime import date, datetime
from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr

from hdr_schemata.definitions.HDRUK import *

class Coverage(BaseModel):
    
    spatial: Optional[str] = Field(
        None,
        title='Spatial'
    )

    physicalSampleAvailability: Optional[CommaSeparatedValues] = Field(
        None,
        title='Physical Sample Availability'
    )

    pathway: Optional[Description] = Field(
        None,
        title='Pathway'
    )
    
    followup: Optional[Followup] = Field(
        None,
        title='Followup'
    )

    typicalAgeRange: Optional[AgeRange] = Field(
        None,
        title='Typical Age Range'
    )
