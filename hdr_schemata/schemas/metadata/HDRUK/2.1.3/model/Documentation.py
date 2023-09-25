from typing import Optional, Union, List
from pydantic import BaseModel, Field
from definitions import *


class Documentation(BaseModel):
    class Config:
        extra = 'forbid'

    description: Optional[Description] = Field(
        None, description='A free-text description of the record.', title='Description'
    )
    
    associatedMedia: Optional[
        Union[Optional[CommaSeparatedValues], List[Optional[Url]]]
    ] = Field(
        None,
        description='Please provide any media associated with the Gateway Organisation using a valid URI for the content. This is an opportunity to provide additional context that could be useful for researchers wanting to understand more about the dataset and its relevance to their research question. The following formats will be accepted .jpg, .png or .svg, .pdf, .xslx or .docx. Note: media asset can be hosted by the organisation or uploaded using the onboarding portal.',
        examples=['PDF Document that describes study protocol'],
        title='Associated Media',
    )
    
    isPartOf: Optional[
        Union[
            Optional[CommaSeparatedValues],
            List[Union[Optional[Url], OneHundredFiftyCharacters, IsPartOfEnum]],
        ]
    ] = Field(
        'NOT APPLICABLE',
        description='Please complete only if the dataset is part of a group or family',
        examples=['Hospital Episodes Statistics datasets (A&E, APC, OP, AC MSDS).'],
        title='Group',
    )
