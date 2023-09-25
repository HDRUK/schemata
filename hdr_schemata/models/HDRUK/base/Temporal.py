from datetime import date,datetime
from typing import Optional, List, Union
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *


class Temporal(BaseModel):
    class Config:
        extra = 'forbid'

    accrualPeriodicity: Periodicity = Field(
        ...,
        description='Please indicate the frequency of distribution release. If a dataset is distributed regularly please choose a distribution release periodicity from the constrained list and indicate the next release date. When the release date becomes historical, a new release date will be calculated based on the publishing periodicity. If a dataset has been published and will remain static please indicate that it is static and indicated when it was released. If a dataset is released on an irregular basis or “on-demand” please indicate that it is Irregular and leave release date as null. If a dataset can be published in real-time or near-real-time please indicate that it is continuous and leave release date as null. Notes: see https://www.dublincore.org/specifications/dublin-core/collection-description/frequency/',
        title='Periodicity',
    )
    distributionReleaseDate: Optional[Union[date, datetime]] = Field(
        None,
        description='Date of the latest release of the dataset. If this is a regular release i.e. quarterly, or this is a static dataset please complete this alongside Periodicity. If this is Irregular or Continuously released please leave this blank. Notes: Periodicity and release date will be used to determine when the next release is expected. E.g. if the release date is documented as 01/01/2020 and it is now 20/04/2020 and there is a quarterly release schedule, the latest release will be calculated as 01/04/2020.',
        title='Release Date',
    )
    startDate: Optional[Union[date, datetime]] = Field(
        ...,
        description='The start of the time period that the dataset provides coverage for. If there are multiple cohorts in the dataset with varying start dates, please provide the earliest date and use the description or the media attribute to provide more information.',
        title='Start Date',
    )
    endDate: Optional[Union[date, datetime, EndDateEnum]] = Field(
        None,
        description='The end of the time period that the dataset provides coverage for. If the dataset is “Continuous” and has no known end date, please state continuous. If there are multiple cohorts in the dataset with varying end dates, please provide the latest date and use the description or the media attribute to provide more information.',
        title='End Date',
    )
    timeLag: TimeLag = Field(
        ...,
        description='Please indicate the typical time-lag between an event and the data for that event appearing in the dataset',
        title='Time Lag',
    )
