from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr
from hdr_schemata.definitions.HDRUK import *


class Revision(BaseModel):

    version: constr(min_length=2,max_length=100) = Field(
        ...,
        description='Version number used for previous version of this dataset',
        example='6.0.0',
        title='revision version'
    )

    url: Url = Field(
        ...,
        description='Some url with a reference to the record of a previous version of this dataset',
        example='https://api.service.nhs.uk/health-research-data-catalogue/datasetrevisions/841f7da2-b018-41f6-b4ae-2e0aadab6561',
        title='revision url'
    )
