from typing import Optional, Union
from pydantic import BaseModel, Field, constr, validator

from hdr_schemata.definitions.SchemaOrg import Text

class GeoCoordinates(BaseModel):

    m_type: Text = Field(
        alias="@type",
        default="GeoCoordinates"
    )

    latitude: constr(pattern=r'^[-]?([0-8]?[0-9]|90)(\.[0-9]+)?$')
    
    longitude: constr(pattern=r'^[-]?((1[0-7][0-9])|([0-9]?[0-9]))(\.[0-9]+)?$')


    @validator('latitude')
    def validate_latitude(cls, value):
        # Ensure latitude is within the valid range (-90 to +90 degrees)
        latitude = float(value)
        if not (-90 <= latitude <= 90):
            raise ValueError('Latitude must be between -90 and +90 degrees')
        return value

    @validator('longitude')
    def validate_longitude(cls, value):
        # Ensure longitude is within the valid range (-180 to +180 degrees)
        longitude = float(value)
        if not (-180 <= longitude <= 180):
            raise ValueError('Longitude must be between -180 and +180 degrees')
        return value
