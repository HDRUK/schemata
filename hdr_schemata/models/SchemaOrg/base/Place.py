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

    eligibleRegion: Optional[Text] = Field(
        None,
        description = 'The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is valid.'
    )
