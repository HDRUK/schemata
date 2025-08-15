from typing import Optional, Union
from pydantic import AnyUrl, BaseModel, EmailStr, Field, constr
from hdr_schemata.definitions.HDRUK import *

from .annotations import annotations

an = annotations.summary.publisher


class Publisher(BaseModel):

    publisherName: Optional[Name] = Field(None, **an.publisherName.__dict__)

    publisherGatewayId: Optional[Union[int, constr(min_length=2, max_length=50)]] = Field(
    None, **an.publisherGatewayId.__dict__
)
