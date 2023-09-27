from typing import Union
from pydantic import BaseModel, Field, AnyUrl

from hdr_schemata.definitions.SchemaOrg import Text,Ror
from hdr_schemata.models.SchemaOrg.base import Organization as BaseOrganization


class Organization(BaseOrganization):
    #overload to require a Ror organisation URL
    sameAs: Union[Ror,AnyUrl] = Field(
        description="Link or ror.org ID of the organisation",
        example="https://ror.org/xxxxxxxxx"
    )
    
