from typing import Optional
from pydantic import Field

from hdr_schemata.definitions.SchemaOrg import Text

from .GeoCoordinates import GeoCoordinates
from .Thing import Thing

class Place(Thing):

    m_type: Text = Field(
        alias="@type",
        default="Place"
    )
    geo: Optional[GeoCoordinates] = Field(
        None,
        description='GeoCoordinates of the place'
    )
