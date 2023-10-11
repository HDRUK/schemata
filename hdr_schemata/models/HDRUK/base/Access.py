from typing import Optional, List, Union
from pydantic import BaseModel, Field, constr
from hdr_schemata.definitions.HDRUK import *

class Access(BaseModel):
    class Config:
        extra = 'forbid'

    accessRights: Optional[LongDescription] = Field(..., title='Access Rights')

    accessService: Optional[LongDescription] = Field(
        None,
        description='Please provide a brief description of the data access services that are available including: environment that is currently available to researchers;additional consultancy and services;any indication of costs associated. If no environment is currently available, please indicate the current plans and timelines when and how data will be made available to researchers Note: This value will be used as default access environment for all datasets submitted by the organisation. However, there will be the opportunity to overwrite this value for each dataset.',
        examples=[
            'https://cnfl.extge.co.uk/display/GERE/Research+Environment+User+Guide'
        ],
        title='Access Service',
    )
    accessRequestCost: Optional[
        Union[Optional[LongDescription], List[Optional[Url]]]
    ] = Field(
        None,
        description='Please provide link(s) to a webpage detailing the commercial model for processing data access requests for the organisation (if available) Definition: Indication of commercial model or cost (in GBP) for processing each data access request by the data custodian.',
        title='Organisation Access Request Cost',
    )
    deliveryLeadTime: Optional[DeliveryLeadTime] = Field(
        None,
        description='Please provide an indication of the typical processing times based on the types of requests typically received.',
        title='Access Request Duration',
    )
    jurisdiction: Union[Optional[CommaSeparatedValues], List[Isocountrycode]] = Field(
        ...,
        description="Please use country code from ISO 3166-1 country codes and the associated ISO 3166-2 for regions, cities, states etc. for the country/state under whose laws the data subjects' data is collected, processed and stored.",
        title='Jurisdiction',
    )
    dataController: Optional[LongDescription] = Field(
        ...,
        description='Data Controller means a person/entity who (either alone or jointly or in common with other persons/entities) determines the purposes for which and the way any Data Subject data, specifically personal data or are to be processed.',
        title='Data Controller',
    )
    dataProcessor: Optional[LongDescription] = Field(
        None,
        description='A Data Processor, in relation to any Data Subject data, specifically personal data, means any person/entity (other than an employee of the data controller) who processes the data on behalf of the data controller.',
        title='Data Processor',
    )
