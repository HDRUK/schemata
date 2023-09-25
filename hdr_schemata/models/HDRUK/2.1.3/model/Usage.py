from typing import Optional, Union, List
from pydantic import BaseModel, Field
from hdr_schemata.definitions.HDRUK import *

class Usage(BaseModel):
    class Config:
        extra = 'forbid'

    dataUseLimitation: Optional[
        Union[Optional[CommaSeparatedValues], List[DataUseLimitation]]
    ] = Field(
        None,
        description='Please provide an indication of consent permissions for datasets and/or materials, and relates to the purposes for which datasets and/or material might be removed, stored or used. NOTE: we have extended the DUO to include a value for NO LINKAGE',
        title='Data Use Limitation',
    )
    dataUseRequirements: Optional[
        Union[Optional[CommaSeparatedValues], List[DataUseRequirements]]
    ] = Field(
        None,
        description='Please indicate fit here are any additional conditions set for use if any, multiple requirements may be provided. Please ensure that these restrictions are documented in access rights information.',
        title='Data Use Requirements',
    )
    resourceCreator: Optional[
        Union[Optional[ShortDescription], List[Optional[ShortDescription]]]
    ] = Field(
        None,
        description='Please provide the text that you would like included as part of any citation that credits this dataset. This is typically just the name of the publisher.   No employee details should be provided.',
        title='Citation Requirements',
    )
    investigations: Optional[
        Union[Optional[CommaSeparatedValues], List[Optional[Url]]]
    ] = Field(None, title='Investigations')
    isReferencedBy: Optional[Union[Optional[Doi], str, List[Optional[Doi]]]] = Field(
        None,
        description='Please provide the keystone paper associated with the dataset. Also include a list of known citations, if available and should be links to existing resources where the dataset has been used or referenced. Please provide multiple entries, or if you are using a csv upload please provide them as a tab separated list.',
        title='Citations',
    )
