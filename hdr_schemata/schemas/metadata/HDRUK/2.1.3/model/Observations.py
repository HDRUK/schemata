from datetime import datetime, date
from typing import Optional, Union, List
from pydantic import BaseModel, Field
from definitions import *


class Observation(BaseModel):
    class Config:
        extra = 'forbid'

    observedNode: StatisticalPopulationConstrained = Field(
        ...,
        description='Please select one of the following statistical populations for you observation',
        examples=['PERSONS'],
        title='Statistical Population',
    )
    measuredValue: int = Field(
        ...,
        description='Please provide the population size associated with the population type the dataset i.e. 1000 people in a study, or 87 images (MRI) of Knee Usage Note: Used with Statistical Population, which specifies the type of the population in the dataset.',
        title='Measured Value',
    )
    disambiguatingDescription: Optional[AbstractText] = Field(
        None,
        description='If SNOMED CT term does not provide sufficient detail, please provide a description that disambiguates the population type.',
        title='Disambiguating Description',
    )
    observationDate: Union[date, datetime] = Field(
        ...,
        description='Please provide the date that the observation was made. Some datasets may be continuously updated and the number of records will change regularly, so the observation date provides users with the date that the analysis or query was run to generate the particular observation. Multiple observations can be made i.e. an observation of cumulative COVID positive cases by specimen on the 1/1/2021 could be 2M. On the 8/1/2021 a new observation could be 2.1M. Users can add multiple observations.',
        title='Observation Date',
    )
    measuredProperty: MeasuredProperty = Field(
        ...,
        description='Initially this will be defaulted to "COUNT"',
        title='Measured Property',
    )
