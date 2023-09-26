from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

class Usage(BaseModel):
    class Config:
        extra = 'forbid'

    #note: is this useful? Is there not a better way of doing this?
    #      is it better as a part of the AccessService?
    #      should it be a CommaSeparatedValues where the values are limited?
    #      Optional[CommaSeparated[DataUseLimitation]]
    #      see: https://github.com/HDRUK/schemata-2/blob/master/hdr_schemata/definitions/HDRUK/DataUseLimitation.py  
    dataUseLimitation: Optional[CommaSeparatedValues] = Field(
        ...,
        description='Any restrictions to its usage',
        example="GENERAL RESEARCH USE,PROJECT SPECIFIC RESTRICTIONS",
        title='Data Use Limitation',
    )

    #note: exisitng metadata is referencing 'restrictions' - are these not Limitations too?
    #      as above, this could be limited to allowed Enum values? Instead of arbitrary CommaSeparatedValues
    dataUseRequirement: Optional[CommaSeparatedValues] = Field(
        ...,
        description='Any requirements needed for data usage',
        example="PROJECT SPECIFIC RESTRICTIONS,TIME LIMIT ON USE,USER SPECIFIC RESTRICTION",
        title='Data Use Requirements',
    )

    #note: wouldnt be want to link this to an Organisation/Person/DataCustodian Account?
    #      we are we letting this just be a ShortDescription?
    resourceCreator: Optional[ShortDescription] = Field(
        None,
        description='Who has created this resource',
        example="Ministry of Justice",
        title='Resource Creator',
    )
