from typing import Optional, List, Union
from pydantic import BaseModel, Field, constr
from hdr_schemata.definitions.HDRUK import *

class Access(BaseModel):
    class Config:
        extra = 'forbid'

    #note: do we want to make this CommaSeparatedValues of URLs?
    #      dont allow a description of the license?
    accessRights: Optional[CommaSeparatedValues] = Field(
        ...,
        description='Optional link(s) or a description of where the license associated to accessing this dataset',
        example='https://raw.githubusercontent.com/HDRUK/papers/master/LICENSE',
        title='Access Rights'
    )

    #note: do we want to limit these to actual accessibly service objects?
    #      e.g.: Optional[AccessServiceEnum]
    #      options: [SAIL,HIC,DARE,...,OTHER]
    #
    #note: do we want to include something accessServiceType (?)
    #      options: [TRE, SDE, University, SafeHaven, ... ]
    accessService: Optional[LongDescription] = Field(
        None,
        description='',
        example="The SAIL Databank is powered by the UK Secure e-Research Platform (UKSeRP). Following approval through safeguard processes, access to project-specific data within the secure environment is permitted using two-factor authentication.",
        title='Access Service',
    )


    #note: as above... having a long description seems odd to me...
    #      we could associate this with an Optional[AccessService]
    #      class AccessService(BaseModel):
    #            serviceName: ShortTitle
    #            serviceDescription: LongDescription
    #            cost: 'free'|'paid'|'other'
    #            timeToAcess: DeliveryLeadTime
    accessRequestCost: Optional[LongDescription] = Field(
        None,
        description='',
        example="Data provision is free from SAIL. Overall project costing depends on the number of people that require access to the SAIL Gateway, the activities that SAIL needs to complete (e.g. loading non-standard datasets), data refreshes, analytical work required, disclosure control process, and special case technological requirements.",
        title='Organisation Access Request Cost',
    )

    #note: related to above... this is hard to know or guess..
    #      not useful to a researcher as they can tell this is made up...
    #      may remove or class as a 'AccessService'
    deliveryLeadTime: Optional[DeliveryLeadTime] = Field(
        None,
        description='An arbitrary guess at the time to gain access to the dataset...',
        example='2-6 MONTHS',
        title='Access Request Duration',
    )

    #note: May want to make this a CommaSeparetedListIsoCountryCode
    #       e.g. GB-XXX
    jurisdiction: Optional[CommaSeparatedValues] = Field(
        ...,
        description="Comma separated country codes of where the data jurisdiction is.",
        example="GB-WLS,GB-GBN,GB-SCT",
        title='Jurisdiction',
    )

    #note: this could also be associated with the AccessService?
    #      could the dataController not be the TRE for example?
    #      terminology could be confusing here... 
    dataController: Optional[LongDescription] = Field(
        ...,
        description="Name of the data controller",
        example="SAIL Databank",
        title='Data Controller',
    )

    #note: as with dataController-- what does this mean?
    #      are these often different?
    dataProcessor: Optional[LongDescription] = Field(
        None,
        description='Name of the data processors',
        example='SAIL Databank',
        title='Data Processor',
    )
