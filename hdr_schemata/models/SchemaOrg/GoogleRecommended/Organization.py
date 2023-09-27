from typing import Union, Optional
from pydantic import BaseModel, Field, AnyUrl

from hdr_schemata.definitions.SchemaOrg import Text,Ror
from hdr_schemata.models.SchemaOrg.base import Organization as BaseOrganization


class Organization(BaseOrganization):
    #overload to require a Ror organisation URL
    sameAs: Optional[Union[Ror,AnyUrl]] = Field(
        None,
        description="Link or ror.org ID of the organisation",
        example="https://ror.org/xxxxxxxxx"
    )
    
