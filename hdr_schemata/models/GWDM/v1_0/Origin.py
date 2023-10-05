from typing import Optional, List, Union
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

class Origin(BaseModel):
    class Config:
        extra = 'forbid'

    #note: shall we update to limit to: https://github.com/HDRUK/schemata-2/blob/master/hdr_schemata/definitions/HDRUK/Purpose.py
    purpose: Optional[CommaSeparatedValues] = Field(
        None,
        description='Indicates the purpose(s) that the dataset was collected.',
        example='ADMINISTRATIVE,STATUTORY',
        title='Purpose',
    )

    #note: update to limit to: https://github.com/HDRUK/schemata-2/blob/master/hdr_schemata/definitions/HDRUK/Source.py
    source: Optional[CommaSeparatedValues] = Field(
        None,
        description='Indicates the source of the data extraction',
        example= "PAPER BASED,ELECTRONIC SURVEY",
        title='Source',
    )
    
    #note: update to limit to: https://github.com/HDRUK/schemata-2/blob/master/hdr_schemata/definitions/HDRUK/Setting.py
    collectionSituation: Optional[CommaSeparatedValues] = Field(
        None,
        description='Indicate the setting(s) where data was collected. Multiple settings may be provided',
        example="IN-PATIENTS,PRIMARY CARE",
        title='Setting',
    )


