from typing import Optional,Union,List
from pydantic import BaseModel, Field
from definitions import *

class Organisation(BaseModel):
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
    accessRights: Optional[Union[Optional[Url], List[Optional[Url]]]] = Field(
        None,
        description='The URL of a webpage where the data access request process and/or guidance is provided. If there is more than one access process i.e. industry vs academic please provide both.',
        title='Organisation Default Access Rights',
    )
    deliveryLeadTime: Optional[DeliveryLeadTime] = Field(
        None,
        description='Please provide an indication of the typical processing times based on the types of requests typically received. Note: This value will be used as default access request duration for all datasets submitted by the organisation. However, there will be the opportunity to overwrite this value for each dataset.',
        title='Access Request Duration',
    )
    accessService: Optional[LongDescription] = Field(
        None,
        description='Please provide a brief description of the data access services that are available including: environment that is currently available to researchers;additional consultancy and services;any indication of costs associated. If no environment is currently available, please indicate the current plans and timelines when and how data will be made available to researchers Note: This value will be used as default access environment for all datasets submitted by the organisation. However, there will be the opportunity to overwrite this value for each dataset.',
        examples=[
            'https://cnfl.extge.co.uk/display/GERE/Research+Environment+User+Guide'
        ],
        title='Organisation Access Service',
    )
    accessRequestCost: Optional[
        Union[Optional[ShortDescription], List[Optional[Url]]]
    ] = Field(
        None,
        description='Please provide link(s) to a webpage or a short description detailing the commercial model for processing data access requests for the organisation (if available) Definition: Indication of commercial model or cost (in GBP) for processing each data access request by the data custodian.',
        title='Organisation Access Request Cost',
    )
    dataUseLimitation: Optional[
        Union[Optional[CommaSeparatedValues], List[DataUseLimitation]]
    ] = Field(
        None,
        description='Please provide an indication of consent permissions for datasets and/or materials, and relates to the purposes for which datasets and/or material might be removed, stored or used. Notes: where there are existing data-sharing arrangements such as the HDR UK HUB data sharing agreement or the NIHR HIC data sharing agreement this should be indicated within access rights. This value will be used as terms for all datasets submitted by the organisation. However, there will be the opportunity to overwrite this value for each dataset.',
        title='Data Use Limitation',
    )
    dataUseRequirements: Optional[
        Union[Optional[CommaSeparatedValues], List[DataUseRequirements]]
    ] = Field(
        None,
        description='Please indicate fit here are any additional conditions set for use if any, multiple requirements may be provided. Please ensure that these restrictions are documented in access rights information.',
        title='Data Use Requirements',
    )
