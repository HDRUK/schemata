from datetime import date,datetime
from typing import Optional, List, Union
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *


class Temporal(BaseModel):
    class Config:
        extra = 'forbid'

        
    startDate: Optional[Union[date, datetime]] = Field(
        ...,
        description='.',
        title='Start Date',
    )
    endDate: Optional[Union[date, datetime]] = Field(
        None,
        description='.',
        title='End Date',
    )
    timeLag: TimeLag = Field(
        ...,
        description='t',
        title='Time Lag',
    )
        
    accrualPeriodicity: Periodicity = Field(
        ...,
        description='',
        title='Periodicity',
    )
    distributionReleaseDate: Optional[Union[date, datetime]] = Field(
        None,
        description='',
        title='Release Date',
    )
