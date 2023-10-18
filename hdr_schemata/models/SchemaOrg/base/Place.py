from typing import Optional, Union
from pydantic import AnyUrl, BaseModel, RootModel, Field,  EmailStr

from hdr_schemata.definitions.SchemaOrg import Text

from .GeoCoordinates import GeoCoordinates

class Place(BaseModel):

    m_type: Text = Field(
        alias="@type",
        default="Place"
    )
    geo: Optional[GeoCoordinates] = Field(
        None,
        description='GeoCoordinates of the place'
    )
