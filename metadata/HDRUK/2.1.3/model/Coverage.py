from typing import Optional, List, Union
from pydantic import BaseModel, Field
from definitions import *

class Coverage(BaseModel):
    class Config:
        extra = 'forbid'

    spatial: Optional[
        Union[Optional[CommaSeparatedValues], List[Optional[Url]]]
    ] = Field(
        None,
        description='The geographical area covered by the dataset. It is recommended that links are to entries in a well-maintained gazetteer such as https://www.geonames.org/ or https://what3words.com/daring.lion.race.',
        examples=[
            'https://www.geonames.org/2635167/united-kingdom-of-great-britain-and-northern-ireland.html'
        ],
        title='Geographic Coverage',
    )
    typicalAgeRange: Optional[AgeRange] = Field(
        None,
        description="Please indicate the age range in whole years of participants in the dataset. Please provide range in the following format '[min age] – [max age]' where both the minimum and maximum are whole numbers (integers).",
        title='Age Range',
    )
    physicalSampleAvailability: Optional[
        Union[Optional[CommaSeparatedValues], List]
    ] = Field(
        None,
        description='Availability of physical samples associated with the dataset. If samples are available, please indicate the types of samples that are available. More than one type may be provided. If sample are not yet available, please provide “AVAILABILITY TO BE CONFIRMED”. If samples are not available, then please provide “NOT AVAILABLE”.',
        examples=['BONE MARROW'],
        title='Physical Sample Availability',
    )
    followup: Optional[Followup] = Field(
        'UNKNOWN',
        description='If known, what is the typical time span that a patient appears in the dataset (follow up period)',
        title='Followup',
    )
    pathway: Optional[Description] = Field(
        None,
        description='Please indicate if the dataset is representative of the patient pathway and any limitations the dataset may have with respect to pathway coverage. This could include if the dataset is from a single speciality or area, a single tier of care, linked across two tiers (e.g. primary and secondary care), or an integrated care record covering the whole patient pathway.',
        title='Pathway',
    )
