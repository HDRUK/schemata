from typing import Optional, Union, List
from pydantic import AnyUrl, BaseModel, RootModel, Field,  EmailStr

from hdr_schemata.definitions.SchemaOrg import Text

class DataCatalog(BaseModel):
    """
    This is pretty incomplete, but we might not need it... 
    """

    m_type: Text = Field(
        alias="@type",
        default="DataCatalog"
    )

    name: Text = Field(
        ...,
        description="The name of the item."
    )
    
