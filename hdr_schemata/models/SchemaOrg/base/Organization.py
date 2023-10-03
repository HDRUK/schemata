from typing import Union, Optional
from pydantic import BaseModel, Field, AnyUrl, EmailStr

from hdr_schemata.definitions.SchemaOrg import Text

from .Thing import Thing

class Organization(Thing):
    
    m_type: Text = Field(
        alias="@type",
        default="Organization"
    )

    email: Optional[EmailStr] = Field(
        None,
        description="Email address.",
    )

    legalName: Optional[Text] = Field(
        None,
        description="Legal name of the organisation",
        example="Fictitious Research Consortium"
    )

