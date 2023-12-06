from typing import Optional,Union,List
from pydantic import BaseModel, Field

from hdr_schemata.definitions.HDRUK import *

class Organisation(BaseModel):
     class Config:
          extra = 'forbid'
          
     identifier: Optional[Url] = Field(
          None,
          description='Please provide a Grid.ac identifier (see https://www.grid.ac/institutes) for your organisation. If your organisation does not have a Grid.ac identifier please use the “suggest and institute” function here: https://www.grid.ac/institutes#',
          title='Organisation Identifier',
     )
     name: OneHundredFiftyCharacters = Field(
          ..., description='Name of the organisation', title='Organisation Name'
     )
     logo: Optional[Url] = Field(
          None,
          description='Please provide a logo associated with the Gateway Organisation using a valid URL. The following formats will be accepted .jpg, .png or .svg.',
          title='Organisation Logo',
     )
     description: Optional[Description] = Field(
          None,
          description='Please provide a URL that describes the organisation.',
          title='Organisation Description',
     )
     contactPoint: Union[Optional[EmailAddress], List[Optional[EmailAddress]]] = Field(
          ...,
          description='Organisation contact point(s)',
          title='Organisation Contact Point',
     )
     memberOf: Optional[MemberOf] = Field(
          None,
          description='Please indicate if the organisation is an Alliance Member or a Hub.',
          title='Organisation Membership',
     )
     
