from typing import Optional, List, Union
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

class Origin(BaseModel):
    class Config:
        extra = 'forbid'

    purpose: Optional[CommaSeparatedValues] = Field(
        None,
        description='Pleases indicate the purpose(s) that the dataset was collected.',
        title='Purpose',
    )
    source: Optional[CommaSeparatedValues] = Field(
        None,
        description='Pleases indicate the source of the data extraction',
        title='Source',
    )
    collectionSituation: Optional[CommaSeparatedValues] = Field(
        None,
        description='Pleases indicate the setting(s) where data was collected. Multiple settings may be provided',
        title='Setting',
    )


