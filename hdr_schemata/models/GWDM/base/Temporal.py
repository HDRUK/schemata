from datetime import date,datetime
from typing import Optional, List, Union
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *


class Temporal(BaseModel):
    class Config:
        extra = 'forbid'

        
    startDate: Optional[Union[date, datetime]] = Field(
        ...,
        description='The start of the time period that the dataset provides coverage for',
        example='12/03/2020',
        title='Start Date',
    )
    endDate: Optional[Union[date, datetime]] = Field(
        None,
        description='The end of the time period that the dataset provides coverage for',
        example='12/03/2020',
        title='End Date',
    )
    timeLag: TimeLag = Field(
        ...,
        description='Rypical time-lag between an event and the data for that event appearing in the dataset',
        example="LESS 1 WEEK",
        title='Time Lag',
    )
        
    accrualPeriodicity: Periodicity = Field(
        ...,
        description='frequency of distribution release. If a dataset is distributed regularly please choose a distribution release periodicity from the constrained list and indicate the next release date. When the release date becomes historical, a new release date will be calculated based on the publishing periodicity.',
        example="MONTHLY",
        title='Periodicity',
    )
    
    distributionReleaseDate: Optional[Union[date, datetime]] = Field(
        None,
        description='Date of the latest release of the dataset. If this is a regular release i.e. quarterly, or this is a static dataset please complete this alongside Periodicity.',
        title='Release Date',
    )
