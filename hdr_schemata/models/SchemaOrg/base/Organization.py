from typing import Union
from pydantic import BaseModel, Field, AnyUrl

from hdr_schemata.definitions.SchemaOrg import Text,Ror

class Organization(BaseModel):
    
    _type: Text = Field(
        alias="@type",
        default="Organization"
    )

    sameAs: Union[Ror,AnyUrl] = Field(
        description="Link or ror.org ID of the organisation",
        example="https://ror.org/xxxxxxxxx"
    )
    
    name: Text = Field(
        description="Name of the organisation",
        example="Fictitious Research Consortium"
    )

